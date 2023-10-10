from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    queryset = todo.objects.all()
    serializer_class = TodoSerializer

class UserView(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer

class OtpView(viewsets.ModelViewSet):
    queryset = otp.objects.all()
    serializer_class = OtpSerializer