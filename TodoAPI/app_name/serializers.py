from rest_framework import serializers
from .models import todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = todo
        fields = ('id','url', 'name', 'done','deadline')


class DeadlineTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = ('name', 'done')

class TodoGroupSerializer(serializers.Serializer):
    deadline = serializers.DateTimeField()
    todo_count = serializers.IntegerField()
    todos = DeadlineTodoSerializer(many=True)