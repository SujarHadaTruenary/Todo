from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
import  json

# Create your views here.

class TodoView(viewsets.GenericViewSet):
    queryset = todo.objects.all()
    serializer_class = TodoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class UserView(viewsets.GenericViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer

    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')


        data = user.objects.get(email=email)
        if data.DoesNotExist:
            return Response({'error': 'Invalid email'}, status=status.HTTP_400_BAD_REQUEST)

        if not data.check_password(password):
            return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)

        if not data.verified:
            return Response({'error': 'User is not verified'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(json.dumps(user), status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class OtpView(viewsets.GenericViewSet):
    queryset = otp.objects.all()
    serializer_class = OtpSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def reset_created_at(self, request, *args, **kwargs):
        email = request.data.get('email')
        code = request.data.get('code')

        try:
            instance = otp.objects.get(email=email)
        except otp.DoesNotExist:
            return Response({'error': 'Invalid email'}, status=status.HTTP_400_BAD_REQUEST)

        instance.code = code
        instance.created_at = timezone.now()
        instance.save()

        return Response(status=status.HTTP_200_OK)

    def verify_otp(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        code = serializer.data['code']

        try:
            obj = otp.objects.get(email=email, code=code)
        except otp.DoesNotExist:
            data = {{'error': 'Invalid OTP'}}
            return Response(json.dumps(data), status=status.HTTP_400_BAD_REQUEST)

        if obj.created_at < timezone.now() - timezone.timedelta(minutes=5):
            return Response(json.dumps({'error': 'OTP expired'}), status=status.HTTP_400_BAD_REQUEST)

        # If everything is successful, return a success message in JSON format
        return Response(json.dumps({'success': True}), status=status.HTTP_200_OK)