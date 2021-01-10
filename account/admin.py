from django.contrib import admin
from .models import Address, BusinessType, CustomerProfile, MerchantProfile, Membership

admin.site.register(Address)
admin.site.register(CustomerProfile)
admin.site.register(Membership)

@admin.register(MerchantProfile)
class MerchantProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('merchant_name',)}

@admin.register(BusinessType)
class BusinessTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('type',)}