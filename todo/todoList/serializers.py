

from .models import Todo
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['task','eta','complete']
    

class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','task','eta','complete']
    
    
class TodoShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'