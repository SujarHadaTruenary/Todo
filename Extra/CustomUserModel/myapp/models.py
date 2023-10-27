from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self , phone_number , password = None , **extra_fields):
        if not phone_number:
            raise ValueError("Phone Number is Required")

        if 'email' in extra_fields:
            extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self. model(phone_number = phone_number , **extra_fields)
        user.set_password(password)
        user.save(using = self.db)

        return user

    def create_superuser(self , phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active',True)

        return self.create_user(phone_number,password,**extra_fields)



class CustomUser(AbstractUser):

    username = None
    phone_number = models.CharField(max_length=100 , unique=True)
    email = models.EmailField(max_length=50)
    user_bio = models.CharField(max_length=50)
    user_profile_image = models.ImageField(upload_to="profile")

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['email']

    object = UserManager()






