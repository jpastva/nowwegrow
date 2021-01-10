''' Views for orders app '''
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem, Order
from register.models import User
from cart.cart import Cart
from account.models import Address
from django.contrib import messages

def order_create(request):
    ''' View to create new orders '''
    cart = Cart(request)

    # make sure user is signed in
    if request.user.is_authenticated:
        addresses = Address.objects.filter(user=request.user)
        # check for addresses associated with account
        if addresses:
            if request.method == 'POST':
                # Get chosen address to associate with order
                address_id = request.POST.get("add_id")
                chosen_address = Address.objects.get(id = address_id)
                order = Order()
                order.user = User.objects.get(id = request.user.id)
                order.address = chosen_address
                order.total = 0
                order.active = False
                order.save()
                # Create order items from shopping cart
                for item in cart:
                    OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
                    order.total += item['price']*item['quantity']
                order.save()
                request.session['cart'] = cart
                #clear the cart
                cart.clear()
                # set the order in the session
                request.session['order_id'] = order.id
                
                # redirect for payment
                return redirect(reverse('payment:process'))
            else:
                # Return addresses to let user select during checkout
                return render(request, 'orders/order/create.html', {'addresses': addresses})
        else:
            # Make user add addresses to account
            messages.add_message(request, messages.ERROR,'Please add an address to your account.')
            return render(request, 'account/addresses.html')  
    else:
        # Redirect for user login or signup
        return render(request, 'register/signup.html', {'cart': cart })

def redirect_checkout(request):
    # Customer signup redirect
    response = redirect('register/signup/customer/')
    return response