from rest_framework import serializers
from .models import todolist

class todo_serializer(serializers.ModelSerializer):
    class Meta:
        model = todolist
        fields = '__all__'