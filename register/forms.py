''' Forms for register app '''
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from register.models import User
from account.models import CustomerProfile, MerchantProfile

class CustomerSignUpForm(UserCreationForm):
    ''' Customer sign up form '''
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=75, required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        ''' Save user record and create new customer record '''
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        new_customer = CustomerProfile.objects.create(user=user)
        new_customer.save()
        return user

class MerchantSignUpForm(UserCreationForm):
    ''' Merchant sign up form '''
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=75, required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit = True):
        ''' Save user record and create new merchant record '''
        user = super().save(commit=False)
        user.is_merchant = True
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        new_merchant = MerchantProfile.objects.create(user=user)
        # Populate merchant name with unique info to prevent slug conflicts
        new_merchant.merchant_name = user.first_name + user.last_name + user.email
        new_merchant.save()
        return user
