from rest_framework import serializers
from todo.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = "__all__"

class ToDoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        exclude = ['user',]