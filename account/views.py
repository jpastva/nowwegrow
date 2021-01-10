''' Views for Account app, including methods for customer and mechant operations in user dashboard '''
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import CustomerProfile, MerchantProfile, Address, BusinessType, Membership
from orders.models import OrderItem, Order
from .forms import AddAddressForm, CustomerEditForm, MerchantEditForm, UserEditForm, ProductEditForm, GetIDForm, AddProductForm
from datetime import datetime, timedelta, timezone
from django.contrib import messages
from orders.tasks import order_created
from django.template.defaultfilters import slugify
from register.models import User
from shop.models import Product
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

@login_required
def edit(request):
    ''' View for profile edit functionality '''
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        # Check if user is customer or merchant and validate appropriate forms
        if request.user.is_customer:
            customer = CustomerProfile.objects.get(user=request.user)
            profile_form = CustomerEditForm(instance=customer, data=request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()

                messages.add_message(request, messages.SUCCESS,'Your profile has been updated.')

            else:
                # Redirect for bad form
                messages.add_message(request, messages.ERROR, 'There was a problem with your entry. Please try again.')

            return render(request,'account/dashboard.html', {'user_form': user_form, 'profile_form': profile_form})

        elif request.user.is_merchant:
            merchant = MerchantProfile.objects.get(user=request.user)
            profile_form = MerchantEditForm(instance=merchant, data=request.POST, files=request.FILES)
        
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()

                cd = profile_form.cleaned_data
                # Update slug for merchant profile page
                merchant.slug = slugify(cd['merchant_name']) 
                merchant.save()
                profile_form.save()
            
                messages.add_message(request, messages.SUCCESS,'Your profile has been updated.')

            else:
                # Redirect for bad form
                messages.add_message(request, messages.ERROR, 'There was a problem with your entry. Please try again.')

            return render(request,'account/dashboard.html', {'user_form': user_form, 'profile_form': profile_form})
                
        else:
            user_form = UserEditForm(instance=request.user, data=request.POST)
            if user_form.is_valid():
                user_form.save()

                messages.add_message(request, messages.SUCCESS,'Your profile has been updated.')
            
            else:
                # Redirect for bad form
                messages.add_message(request, messages.ERROR, 'There was a problem with your entry. Please try again.')
        
            return render(request,'account/edit.html', {'user_form': user_form})

    else:
        user_form = UserEditForm(instance=request.user)

        # Check if user is a customer or merchant and generate appropriate form with pre-populated fields
        if request.user.is_customer:
            customer = CustomerProfile.objects.get(user=request.user)
            profile_form = CustomerEditForm(instance=customer)
            
            return render(request,'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})
        
        elif request.user.is_merchant:
            merchant = MerchantProfile.objects.get(user=request.user)
            
            profile_form = MerchantEditForm(instance=merchant)
            
            return render(request,'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})
        
        else:
            return render(request,'account/edit.html', {'user_form': user_form})

@login_required
def dashboard(request):
    ''' View to render dashboard page '''
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

@login_required
def PasswordChangeView(request):
    ''' View for user to change login password '''
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            # Redirect for bad form
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change_form.html', {'form': form})

@login_required
def user_orders(request):
    ''' View to list all user orders '''
    if request.method == 'POST':
        # Process for deleting selected order
        order_id = request.POST.get("order_id", None)
        order = Order.objects.get(id = order_id)
        now =  datetime.now(timezone.utc)
        check_date = now - timedelta(hours=48)

        # Check if order is within cancellation window
        if order.created < check_date:
            messages.add_message(request, messages.ERROR,'Sorry, it is too late to cancel your order.')
            return render (request, 'account/deleteorder.html')
    
        else:
            messages.add_message(request, messages.SUCCESS, 'Your order has been cancelled.')
            order.active = False
            order.save()
            return render (request, 'account/deleteorder.html')
    else:
        # Retrieve user's orders
        orders = Order.objects.filter(user=request.user)
        return render(request, 'account/orders.html', {'orders': orders})

@login_required
def MerchantOrders(request):
    ''' View to list all orders for a merchant's products '''
    products = Product.objects.filter(merchant=request.user)
    # Retrieve order items, as one order can include items from other merchants
    order_items = OrderItem.objects.filter(product__in = products)

    return render(request, 'account/merchants/orderlist.html', {'order_items': order_items})

@login_required
def OrderItems(request):
    ''' View to list all items from a specific order '''
    order_id = request.GET.get("order_id", None)
    items = OrderItem.objects.filter(order__id = order_id)
    return render(request, 'account/orderitems.html', {'items':items})

@login_required
def UserAddresses(request):
    ''' View to list all user addresses '''
    if request.method == 'POST':
        # Process to delete a selected address
        address_id = request.POST.get("address_id", None)
        address = Address.objects.get(id = address_id)
        address.delete()

        messages.add_message(request, messages.SUCCESS,'Your address has been deleted.')
        return render (request, 'account/deleteaddress.html')

    else:
        # Retrieve all user's addresses
        addresses = Address.objects.filter(user=request.user)
        return render(request, 'account/addresses.html', {'addresses': addresses})

@login_required
def AddAddress(request):
    ''' View to allow users to add and manage addresses '''
    if request.method == 'POST':
        address_form = AddAddressForm(data=request.POST)
        if address_form.is_valid():
            new_address = address_form.save(commit=False)
            # Populate address user before saving
            new_address.user = request.user
            new_address.save()
            
            messages.add_message(request, messages.SUCCESS,'Your address has been added.')
            return render(request,'account/dashboard.html')
        else:
            # Redirect for bad form
            messages.add_message(request, messages.ERROR,'There was a problem with your address. Please try again.')
            return render(request,'account/dashboard.html')
    else:
        address_form = AddAddressForm(instance=request.user, data=request.POST)
        return render(request,'account/addaddress.html', {'address_form': address_form})

@login_required
def MembershipView(request):
    ''' View to allow merchant to manage membership '''
    if request.method == 'POST':
        # Process to add a membership
        merchant = MerchantProfile.objects.get(user=request.user)
        # Retrieve specific membership product for order
        memb_prod = Product.objects.get(name__icontains="NowWeGrow Membership")

        address_id = request.POST.get("add_id")
        chosen_address = Address.objects.get(id = address_id)

        # create order for membership
        order = Order()
        order.user = User.objects.get(id = request.user.id)
        order.address = chosen_address
        order.total = memb_prod.unit_price
        order.save()

        order_item = OrderItem()
        order_item.order = order
        order_item.product = memb_prod
        order_item.price = memb_prod.unit_price
        order_item.save()

        # create membership
        membership = Membership()
        membership.merchant = merchant
        membership.price = memb_prod.unit_price
        membership.active = False
        membership.order = order
        membership.save()
        merchant.is_active = False
        merchant.save()
            
        # launch asynchronous task
        order_created.delay(order.id)
            
        # set the order in the session
        request.session['order_id'] = order.id
        request.session['member_id'] = membership.id
            
        # redirect for payment
        return redirect(reverse('payment:process'))
           
    else:
        # Check for membership and whether paid and active
        merchant = MerchantProfile.objects.get(user=request.user)
        membership = Membership.objects.filter(merchant=merchant) 
        addresses = Address.objects.filter(user=request.user)
        memb_prod = Product.objects.get(name__icontains="NowWeGrow Membership")

        if membership:
            membership = get_object_or_404(Membership, merchant=merchant)
            if membership.active:
                messages.add_message(request, messages.SUCCESS, 'Here are your membership details.')
            else:
                # Inactive member
                messages.add_message(request, messages.ERROR, 'Your membership has expired. Please renew to reactivate your profile.') 
        else:
            # No membership exists
            messages.add_message(request, messages.ERROR, 'You do not currently have a membership associated with your account.')

    return render(request, 'account/merchants/membership.html', {'membership': membership, 'addresses': addresses, 'memb_prod': memb_prod})

@login_required
def MembershipRenew(request):
    ''' View for renewal of memberships '''
    if request.method == 'POST':
        # Retrieve order data for membership to renew
        order_id = request.POST.get('order_id', None)
        order_id_clean = int(order_id.replace('Order ', ''))
        order = Order.objects.get(id=order_id_clean)
        membership = Membership.objects.get(id=request.POST.get('mem_id', None))

        # set the order in the session
        request.session['order_id'] = order.id
        request.session['member_id'] = membership.id
            
        # redirect for payment
        return redirect(reverse('payment:process'))

    else:
        # Retrieve order data for membership to display
        order_id = request.GET.get("mem_order")
        order_id_clean = int(order_id.replace('Order ', ''))
        order = Order.objects.get(id=order_id_clean)

        member_id = request.GET.get("mem_id")
        membership = Membership.objects.get(id=member_id)

        # Retrieve membership product to use current price
        memb_prod = Product.objects.get(name__icontains="NowWeGrow Membership")
        
        return render(request, 'account/merchants/membership_renew.html', {'order': order, 'membership': membership, 'memb_prod': memb_prod})

@login_required
def MerchantProducts(request):
    ''' View to list merchant products and allow for edits or removal '''
    if request.method == 'POST':
        product_id = request.POST.get("product_id", None)
        product = Product.objects.get(id = product_id)

        messages.add_message(request, messages.SUCCESS, 'Your product listing has been removed.')
        product.available = False
        product.save()
        return render (request, 'account/dashboard.html')

    else:
        # Retrieve merchant info
        merchant = MerchantProfile.objects.get(user = request.user)
        # Make sure merchant has active membership to list products
        if merchant.is_active:
            # Retrieve merchant's products
            products = Product.objects.filter(merchant=request.user)
            return render(request, 'account/merchants/products.html', {'products': products})
        else:
            # Inactive merchant
            messages.add_message(request, messages.ERROR, 'You cannot list products because you do not have an active membership.')
            return render(request, 'account/dashboard.html')


@login_required
def EditProducts(request):
    ''' View to list merchant products and allow for edits or removal '''
    if request.method == 'POST':
        id_form = GetIDForm(request.POST)
        if id_form.is_valid():

            cd = id_form.cleaned_data
            prod_id = cd['prod_id']

            # Retrieve existing product to edit
            product = Product.objects.get(id = prod_id)

            product_form = ProductEditForm(instance = product, data=request.POST, files=request.FILES)
            if product_form.is_valid():
                messages.add_message(request, messages.SUCCESS, 'Your product has been updated.')
                cd = product_form.cleaned_data
                update_product = product_form.save(commit=False)
                # Update product link based on new name
                update_product.slug = slugify(cd['name'])
                update_product.merchant = request.user
                update_product.save()

                return render(request,'account/dashboard.html')
            else:
                # Redirect for bad form
                messages.add_message(request, messages.ERROR, 'There was a problem with your form.')
                return render(request, 'account/dashboard.html')

        else:
            # Redirect for bad form
            messages.add_message(request, messages.ERROR, 'There was a problem with your form.')
            return render(request,'account/dashboard.html')

    else:
        # Get product info to edit and pre-populate form
        prod_id = request.GET.get("product_id")
        product = Product.objects.get(id=prod_id)
        prod_init = {'id':prod_id, 'name':product.name, 'category':product.category, 'sale_unit':product.sale_unit, 'unit_price':product.unit_price, 'description':product.description, 'available':product.available, 'image':product.image}
        id_init = {'prod_id': prod_id}
        product_form = ProductEditForm(initial=prod_init, instance=product)
        id_form = GetIDForm(initial=id_init)
        return render(request,'account/merchants/editproducts.html', {'product_form': product_form, 'id_form': id_form, 'prod_id':prod_id})


@login_required
def AddProduct(request):
    ''' View to allow merchants to add a product '''
    if request.method == 'POST':
        product_form = ProductEditForm(data=request.POST, files=request.FILES)
        if product_form.is_valid():
            cd = product_form.cleaned_data
            # Create new product for merchant based on form data
            new_product = product_form.save(commit=False)
            # Update product merchant based on user
            new_product.merchant = request.user
            # Create product link based on name
            new_product.slug =  slugify(cd['name']) 
            new_product.save()
            
            messages.add_message(request, messages.SUCCESS,'Your product has been added.')
            return render(request,'account/dashboard.html')
        else:
            # Redirect for bad form
            messages.add_message(request, messages.ERROR,'There was a problem with your product. Please try again.')
            return render(request,'account/merchants/products.html')
    else:
        product_form = AddProductForm()
        return render(request,'account/merchants/addproduct.html', {'product_form': product_form})


def MerchantList(request, type_slug=None):
    ''' View to list all active merchants for public site '''
    merchant_type = None
    types = BusinessType.objects.all()
    # Limit to active merchants
    merchants = MerchantProfile.objects.filter(is_active=True)
    # If a user has selected a merchant type, only retrieve merchants of that type
    if type_slug:
        merchant_type = get_object_or_404(BusinessType, slug=type_slug)
        merchants = merchants.filter(merchant_type=merchant_type)
    return render(request,'account/merchants/list.html', {'merchant_type': merchant_type, 'types': types, 'merchants': merchants})


def merchant_detail(request, id, slug):
    ''' View to display merchant detail page for public site '''
    merchant = get_object_or_404(MerchantProfile, id=id, slug=slug, is_active=True)
    return render(request, 'account/merchants/detail.html', {'merchant': merchant})

