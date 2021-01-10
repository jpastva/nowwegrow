''' URLs for map app '''
from django.urls import path
from map.views import Map

urlpatterns = [
    path('', Map, name='map'),

]