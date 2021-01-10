''' URLs for account app '''
from django.urls import path
from account.views import edit, dashboard, user_orders, OrderItems, AddAddress, UserAddresses, MerchantList, merchant_detail, MembershipView, PasswordChangeView, MerchantProducts, EditProducts, AddProduct, MerchantOrders, MembershipRenew

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('edit/', edit, name='edit'),
    path('orders/', user_orders, name='user_orders'),
    path('orders/items/', OrderItems, name='user_order_items'),
    path('orders/cancel/', user_orders, name='cancel_order'),
    path('products/', MerchantProducts, name='merchant_products'),
    path('products/edit/', EditProducts, name='edit_products'),
    path('products/remove/', MerchantProducts, name='deactivate_product'),
    path('products/add/', AddProduct, name='add_product'),
    path('addresses/', UserAddresses, name='user_addresses'),
    path('addresses/new/', AddAddress, name='add_address'),
    path('membership/', MembershipView, name='merchant_membership'),
    path('membership/renew/', MembershipRenew, name='renew_membership'),
    path('addresses/delete/', UserAddresses, name='delete_address'),
    path('merchants/list/', MerchantList, name='merchant_list'),
    path('merchants/orders/', MerchantOrders, name='merchant_orders'),
    path('password_change/', PasswordChangeView, name='password_change'),
    path('<slug:type_slug>/', MerchantList, name='merchant_list_by_type'),
    path('<int:id>/<slug:slug>/', merchant_detail, name='merchant_detail'),
 
]