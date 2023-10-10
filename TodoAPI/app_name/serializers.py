from rest_framework import serializers
from .models import todo, user, otp

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = todo
        fields = ('id', 'url', 'name', 'done')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = ('id', 'url', 'email', 'uname','password','verify')

class OtpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = otp
        fields = ('id', 'url', 'email', 'code')