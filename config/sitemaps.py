''' Create sitemap for products and merchants '''
from django.contrib.sitemaps import Sitemap
from shop.models import Product
from account.models import MerchantProfile

class ProductSitemap(Sitemap):
    ''' Set up sitemap for products '''
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        ''' Filter by available products '''
        return Product.objects.filter(available=True)

    def lastmod(self, obj):
        return obj.updated

class MerchantSitemap(Sitemap):
    ''' Set up sitemap for merchants '''
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        ''' Filter by active merchants '''
        return MerchantProfile.objects.filter(is_active=True)
        