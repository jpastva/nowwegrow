''' Forms for use in account app '''
from django import forms
from register.models import User
from orders.models import Order
from shop.models import Product
from .models import Address, CustomerProfile, MerchantProfile

class UserEditForm(forms.ModelForm):
    ''' Form to edit user info '''
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class MerchantEditForm(UserEditForm):
    ''' Form to edit merchant info '''
    class Meta:
        model = MerchantProfile
        fields = ('merchant_name', 'merchant_type', 'merchant_phone', 'merchant_email', 'merchant_street', 'merchant_zip', 'merchant_website', 'image', 'description', 'product_url')

class CustomerEditForm(UserEditForm):
    ''' Form to edit customer info '''
    class Meta:
        model = CustomerProfile
        fields = ('customer_phone',)

class AddProductForm(forms.ModelForm):
    ''' Form to add new product '''
    class Meta:
        model = Product
        fields = ('name', 'category', 'sale_unit', 'unit_price', 'description', 'available', 'image')

class ProductEditForm(forms.ModelForm):
    ''' Form to edit existing product '''
    class Meta:
        model = Product
        fields = ('name', 'category', 'sale_unit', 'unit_price', 'description', 'available', 'image')

class GetIDForm(forms.Form):
    ''' Read only form to retrieve product ID '''
    prod_id = forms.CharField(label = 'ID (read only)', widget = forms.TextInput(attrs={'readonly':'readonly'}))

class AddAddressForm(forms.ModelForm):
    ''' Form to add new address '''
    class Meta:
        model = Address
        fields = ('nickname', 'address1', 'address2', 'city', 'state', 'zip')

class EditAddressForm(forms.ModelForm):
    ''' Form to edit existing address '''
    class Meta:
        model = Address
        fields = ('nickname', 'address1', 'address2', 'city', 'state', 'zip')

class GetOrderForm(forms.ModelForm):
    ''' Form to store order ID '''
    class Meta:
        model = Order
        fields = ('id',)