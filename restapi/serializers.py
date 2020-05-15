from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('user', 'created', 'text', 'done', 'unique_id')
        lookup_field = 'unique_id'
