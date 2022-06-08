from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from authentication.api.managers import UserManager
from core.models import TimestampedModel

# Create your models here.
class User(AbstractBaseUser, TimestampedModel, PermissionsMixin):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255, unique=True)
    
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'phone_number',
    ]
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    