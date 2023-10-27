from django.shortcuts import render
from models import *
from rest_framework.views import APIView
from serializer import *
from .models import user, otp
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

# Create your views here.
class register(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            otp_instance = otp.objects.create(email=serializer.validated_data['email'],code='123456')
            otp_instance.save()

            return Response({'msg':'Complete'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class User(APIView):

    def post(self, request,format=None):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        data = user.objects.get(email=email)

        if not data:
            return Response({'error': 'Invalid email'}, status=status.HTTP_400_BAD_REQUEST)

        if not data.password == password :
            return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)

        if not data.verified:
            return Response({'error': 'User is not verified'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)


class OtpView(APIView):
    def post(self, request,format=None):
        serializer = OtpSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data.get('email')
        code = serializer.validated_data.get('code')


        obj = otp.objects.get(email=email, code=code)
        if not obj:
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

        if obj.created_at < timezone.now() - timezone.timedelta(seconds=10):
            return Response({'error': 'OTP expired'}, status=status.HTTP_400_BAD_REQUEST)

        object = user.objects.get(email=email)
        object.verified = True
        object.save()
        return Response({'success': True}, status=status.HTTP_200_OK)

    def put(self, request,format=None):
        serializer = ResetSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data.get('email')
        code = serializer.validated_data.get('code')
        obj = otp.objects.get(email=email)
        obj.code = code
        obj.created_at = timezone.now()
        obj.save()
        return Response({'success': True}, status=status.HTTP_200_OK)

