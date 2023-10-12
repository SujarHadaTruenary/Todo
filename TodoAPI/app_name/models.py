from django.db import models

# Create your models here.
class todo(models.Model):
    name = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.name

class user(models.Model):
    email = models.CharField(max_length=50)
    uname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
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

