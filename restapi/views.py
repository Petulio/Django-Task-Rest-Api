# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('created')
    serializer_class = TaskSerializer
    lookup_field = 'unique_id'
