''' URLs for about app '''
from django.urls import path
from about.views import about, contact

urlpatterns = [
    path('', about, name='about'),
    path('contact/', contact, name='contact'),
]