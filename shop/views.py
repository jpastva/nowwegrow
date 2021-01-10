''' Views for shop app '''
from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from account.models import MerchantProfile
from cart.forms import CartAddProductForm
from shop.forms import SearchForm
from .models import Category, Product

def product_list(request, category_slug=None):
    ''' View to list active products for shop '''
    category = None
    categories = Category.objects.all()
    # Filter by active products
    products = Product.objects.filter(available=True)
    if category_slug:
        # Filter by product category if selected
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_detail(request, id, slug):
    ''' View to display individual product info '''
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    user = product.merchant
    # Get merchant info to display link to merchant profile
    merchant = MerchantProfile.objects.get(user = user)
    # Include form to add product to cart
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form, 'merchant': merchant})


def product_search(request):
    ''' View to search products '''
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Fields to include in search
            search_vector = SearchVector('name', 'category', 'description', 'merchant__merchantprofile__merchant_name')
            search_query = SearchQuery(query)
            results = Product.objects.annotate(search=search_vector, rank=SearchRank(search_vector, search_query)).filter(available=True).filter(search=query).order_by('-rank')
    return render(request, 'shop/search.html', {'form': form, 'query': query, 'results': results})
    