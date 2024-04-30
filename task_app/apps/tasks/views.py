from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializer import TasksSerializer
from .models import Tasks


# Create your views here.
class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tasks.objects.filter(created_by=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
        else:
            print(serializer.errors)
