from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import TasksSerializer
from .models import Tasks
from task_app.apps.users.functions import generate_custom_uuid


# Create your views here.
class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_task_list = Tasks.objects.filter(created_by=self.request.user).order_by('status', '-created_at')
        return user_task_list

    def perform_create(self, serializer):
        if serializer.is_valid():

            serializer.validated_data['id'] = generate_custom_uuid('task')
            serializer.save(created_by=self.request.user)

        else:
            print(serializer.errors)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():

            if instance.created_by != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)

            serializer.save()

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
