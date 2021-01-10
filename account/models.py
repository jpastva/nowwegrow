''' Models for account app - BusinessType, MerchantProfile, Membership, CustomerProfile, Address '''
from django.db import models
from django.conf import settings
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from geopy.geocoders import Nominatim
from register.models import User
from orders.models import Order

class BusinessType(models.Model):
    ''' Merchant business type data '''
    type = models.CharField(max_length=30)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('type',)
        verbose_name = 'type'
        verbose_name_plural = 'types'

    def __str__(self):
        return self.type
    
    def get_absolute_url(self):
        ''' Return URL for merchant type '''
        return reverse('merchant_list_by_type', args=[self.slug])

class MerchantProfile(models.Model):
    ''' Merchant data '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    merchant_name = models.CharField('Merchant Name',max_length=50, unique=True)
    merchant_email = models.EmailField(max_length=75, blank=True)
    merchant_type = models.ManyToManyField(BusinessType, related_name='types_merchant')
    merchant_phone = PhoneNumberField(null=False, blank=False, unique=True)
    merchant_website = models.URLField(max_length=200, blank=True)
    merchant_street = models.CharField(max_length=500)
    merchant_zip = models.CharField(max_length=12, blank=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, default='0')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, default='0')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='merchants/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    product_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.merchant_name

    def get_absolute_url(self):
        return reverse('merchant_detail', args=[self.id, self.slug])
    
    def save(self, **kwargs):
        ''' Get lat and long for merchant address '''
        address = " ".join([self.merchant_street, self.merchant_zip])
        locator = Nominatim(user_agent='nowwegrow')
        location = locator.geocode(address)
        try:
            self.latitude = location.latitude
            self.longitude = location.longitude
        except AttributeError:
            ''' Set lat and long to 0 if bad address entered '''
            self.latitude = 0
            self.longitude = 0
        super().save(**kwargs)

class Membership(models.Model):
    '''Merchant membership'''
    merchant = models.OneToOneField(MerchantProfile, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.PROTECT, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class CustomerProfile(models.Model):
    ''' Customer data '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customer_phone = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Address(models.Model):
    ''' User address data '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField('Nickname', max_length=30, blank=False)
    address1 = models.CharField('Address Line 1', max_length=30, blank=False)
    address2 = models.CharField('Address Line 2', max_length=30, blank=True)
    city = models.CharField('City', max_length=30, blank=True)
    state = models.CharField('State', max_length=30, blank=True)
    zip = models.CharField('Zip code', max_length=12, blank=False)
