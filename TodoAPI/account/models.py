from django.db import models
from django.contrib.auth.models import AbstractUser

class user(AbstractUser):
    email = models.CharField(max_length=50)
    uname = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.uname

class otp(models.Model):
    email = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    #otp = random.randint(100000,999999)

    def __str__(self):
        return self.email