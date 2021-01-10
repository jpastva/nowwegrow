''' Views for about app '''
from django.shortcuts import render

def about(request):
    ''' View to render about page '''
    return render(request, 'about/about.html')

def contact(request):
    ''' View to render contact page '''
    return render(request, 'about/contact.html')