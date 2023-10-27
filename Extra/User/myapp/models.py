from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, phonenumber, password=None, **extra_fields):
        if not phonenumber:
            raise ValueError("Phone Number is required")

        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        # Extra_fields['email'] = self.normalize_email('email')
        user = self.model(phonenumber=phonenumber, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phonenumber, password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        print(extra_fields)
        return self.create_user(phonenumber, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    phonenumber = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)
    user_profile_image = models.ImageField(upload_to='profile')

    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = ['email']

    objects = UserAccountManager()
