from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager


class UserCustomManager(BaseUserManager):
    def create_user(self, phone_number , password=None , **extra_fields):

        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(phone_number = phone_number , **extra_fields)
        user.set_password(password)
        user.save(using =self.db)
        return user

    def create_superuser(self, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('verified', True)

        return self.create_user(password,**extra_fields)

class user(AbstractUser):
    email = models.EmailField(unique= True)
    verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserCustomManager
    def __str__(self):
        return self.username

class otp(models.Model):
    email = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    #otp = random.randint(100000,999999)

    def __str__(self):
        return self.email


