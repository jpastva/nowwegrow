''' Views for cart app '''
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    ''' View to add product to cart '''
    cart = Cart(request)
    # Retrieve added product based on ID
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    # Add item to cart if data is valid
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    # Redirect to cart page
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    ''' View to remove a product from the cart '''
    cart = Cart(request)
    # Retrieve product to remove
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    # Redirect to cart page
    return redirect('cart:cart_detail')

def cart_detail(request):
    ''' View to display items in cart '''
    cart = Cart(request)
    # Allow for updating item quantity in cart
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                          initial={'quantity': item['quantity'],
                          'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})