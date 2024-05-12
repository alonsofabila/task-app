from rest_framework import serializers
from .models import Tasks
from task_app.apps.users.serializer import UserSerializer


class TasksSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Tasks

        fields = ('id', 'title', 'content', 'status', 'created_at', 'created_by')
        extra_kwargs = {'created_by': {'read_only': True}}
