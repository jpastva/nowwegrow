from django.urls import path, include
from register.views import SignUpView, CustomerSignUpView, MerchantSignUpView, done
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/customer/', CustomerSignUpView.as_view(), name='customer_signup'),
    path('signup/merchant/', MerchantSignUpView.as_view(), name='merchant_signup'),
    path('done/', done, name='done'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
