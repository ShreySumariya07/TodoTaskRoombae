from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('createTodo/',views.CreateTodo.as_view(),name='create-todo'),
    path('showTodo/',views.ShowTodo.as_view(),name='show-todo'),
    path('updateTodo/',views.UpdateTodo.as_view(),name="update-todo"),
    path('deleteTodo/',views.DeleteTodo.as_view(),name='delete-todo'),
]
