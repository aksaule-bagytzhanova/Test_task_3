from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from django.db import models
from .models import Task
from .serializers import TaskShowSerilizer, TaskDoneSerilizer, TaskCreateSerilizer, UserSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.filter()
    serializer_class = TaskCreateSerilizer

    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.filter()
    serializer_class = TaskShowSerilizer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class TaskExecute(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.filter()
    serializer_class = TaskShowSerilizer

    def execute(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer