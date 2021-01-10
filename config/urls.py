''' App-level URLs '''
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from register.views import index
from .sitemaps import ProductSitemap, MerchantSitemap
sitemaps = {'products': ProductSitemap, 'merchants': MerchantSitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', include('about.urls')),
    path('accounts/', include('register.urls')),
    path('profile/', include('account.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('map/', include ('map.urls')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('shop/', include('shop.urls')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
