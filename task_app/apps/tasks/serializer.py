from rest_framework import serializers
from .models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks

        fields = ('id', 'title', 'content', 'status', 'status', 'created_at', 'created_by')
        extra_kwargs = {'created_by': {'read_only': True}}
