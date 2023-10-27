from rest_framework import serializers
from .models import user, otp
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id','email', 'uname', 'password')
class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = otp
        fields = ('id','email', 'code', 'created_at')


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id','email','password')


class ResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = otp
        fields = ('email', 'code')

