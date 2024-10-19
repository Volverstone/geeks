from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('tasks/', views.TaskListAPIView.as_view(), name='task_list'),
    path('movies/<int:id>/', views.TaskDetailAPIView.as_view(), name='task_detail'),
]