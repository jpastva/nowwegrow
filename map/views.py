''' Views for map page '''
from django.shortcuts import render
from account.models import MerchantProfile

def Map(request):
    ''' View to render map pins for merchants '''
    # Token from mapbox account
    mapbox_access_token = 'pk.eyJ1IjoianBhc3R2YSIsImEiOiJja2dwbDNvanYwb21hMnFwa2dmOTJhdjQxIn0.SSHG6bQ_ABGeSXuwr9GJjg'
    merchants = MerchantProfile.objects.filter(is_active = True)

    return render(request, 'map.html', { 'mapbox_access_token': mapbox_access_token, 'merchants': merchants} )