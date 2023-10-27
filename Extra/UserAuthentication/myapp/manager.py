from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.models import BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, phone_number , password=None , **extra_fields):
        if not phone_number :
            raise ValueError("Phone Number is required")

        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(phone_number = phone_number , **extra_fields)
        user.set_password(password)
        user.save(using =self.db)
        return user

    def create_superuser(self, phone_number , password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(phone_number,password,**extra_fields)
