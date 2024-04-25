from rest_framework import serializers
from .models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks

        fields = ('title', 'content', 'status', 'status', 'created_at', 'created_by')
