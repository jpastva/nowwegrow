''' Views for register app '''
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView
from register.forms import CustomerSignUpForm, MerchantSignUpForm
from register.models import User

class CustomerSignUpView(CreateView):
    ''' Customer signup view ''' 
    model = User
    form_class = CustomerSignUpForm
    template_name = 'register/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('done')

class MerchantSignUpView(CreateView):
    ''' Merchant signup view '''
    model = User
    form_class = MerchantSignUpForm
    template_name = 'register/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'merchant'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('done')

class SignUpView(TemplateView):
    ''' View to render signup page '''
    template_name = 'register/signup.html'

def index(request):
    ''' View to render index page '''
    return render(request, 'register/index.html')

def done(request):
    ''' View to render signup finished page '''
    return render(request, 'register/signup_done.html')

