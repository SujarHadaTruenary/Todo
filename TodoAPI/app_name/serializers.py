from rest_framework import serializers
from .models import todo, user, otp


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = todo
        fields = ('id','url', 'name', 'done','deadline')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id','email', 'uname', 'password', 'verified')


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


class DeadlineTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = ('name', 'done')

class TodoGroupSerializer(serializers.Serializer):
    deadline = serializers.DateTimeField()
    todo_count = serializers.IntegerField()
    todos = DeadlineTodoSerializer(many=True)