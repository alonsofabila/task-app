from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializer import TasksSerializer
from .models import Tasks
from task_app.apps.users.functions import generate_custom_uuid


# Create your views here.
class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_task_list = Tasks.objects.filter(created_by=self.request.user).order_by('status')
        return user_task_list

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.validated_data['id'] = generate_custom_uuid('task')
            serializer.save(created_by=self.request.user)
        else:
            print(serializer.errors)
