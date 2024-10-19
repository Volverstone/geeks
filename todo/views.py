from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskListAPIView(generics.ListCreateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailAPIView(generics.ListCreateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'