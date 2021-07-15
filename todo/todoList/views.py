import re
from django.core.checks import messages
from rest_framework import serializers
from .serializers import TodoCreateSerializer,TodoShowSerializer,TodoUpdateSerializer
from django.http.response import JsonResponse
from django.shortcuts import render, resolve_url
from rest_framework.serializers import Serializer
from .models import Todo
from rest_framework.views import APIView
from rest_framework import status
import json

class CreateTodo(APIView):

    def post(self,request,*args,**kwargs):
        form_data = json.loads(json.dumps(request.data))
        if not(form_data.__contains__('task')):
            return JsonResponse ({"success":False,"message":"Task field is essential"})
        elif Todo.objects.filter(task__contains=form_data['task']).exists():
            return JsonResponse({"success":False,"message":"Task already added"})
        serializer = TodoCreateSerializer(data=form_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data={
                "success":True,
                "message":"Task is added in the todo list",
            }
            return JsonResponse(data,status = status.HTTP_201_CREATED)
        else:
            data={
                "success":False,
                "message":"Task not added due to some error in data passed"
            }
            return JsonResponse(data,status=status.HTTP_400_BAD_REQUEST)


class UpdateTodo(APIView):

    def put(self,request,*args,**kwargs):
        form_data = json.loads(json.dumps(request.data))
        if not(form_data.__contains__('id')):
            return JsonResponse({"success":False,"message":"Id is essential field"})

        if not(form_data.__contains__('task')):
            return JsonResponse ({"success":False,"message":"Task field is essential"})

        try:
            todo = Todo.objects.get(id=form_data['id'])
        except Todo.DoesNotExist:
            return JsonResponse({"success":False,"message":"task does not exist"})
        
        serializer = TodoUpdateSerializer(todo,data=form_data)
        if serializer.is_valid():
            serializer.save()
            data={
                "success":True,
                "message":"Task details updated",
                "data":serializer.data
            }
            return JsonResponse(data,status=status.HTTP_200_OK)
        else:
            data={
                "success":False,
                "message":"Task details are not updated"
            }
            return JsonResponse(data,status=status.HTTP_400_BAD_REQUEST)

class DeleteTodo(APIView):
    def delete(self,request,*args,**kwargs):
        form_data = json.loads(json.dumps(request.data))
        if not(form_data.__contains__('id')):
            return JsonResponse({"success":False,"message":"Id is an essential field for delete please do send it"})
        
        try:
            todo = Todo.objects.get(id=form_data['id'])
        except Todo.DoesNotExist:
            return JsonResponse({"success":False,"message":"The item in the list does not exist"})
        todo.delete()
        return JsonResponse({"success":True,"message":"The item successfully deleted"})

class ShowTodo(APIView):
    serializer_class = TodoShowSerializer

    def get(self,request,*args,**kwargs):
        todos = Todo.objects.all()
        serializer = TodoShowSerializer(todos,many=True)
        return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)