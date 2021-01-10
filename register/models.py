''' Models for register app '''
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ''' Add user boolean fields for merchants and customers '''
    is_merchant = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

