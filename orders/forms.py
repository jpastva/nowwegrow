''' Froms for orders app '''
from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    ''' Form to create new order '''
    class Meta:
        model = Order
        fields = ['address', 'user', 'total']

class ChooseAddressForm(forms.Form):
    ''' Form to select address for order '''
    add_id = forms.IntegerField()
    