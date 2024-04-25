from django.urls import path, include
from rest_framework import routers
from task_app.apps.tasks import views


# Api versioning
router = routers.DefaultRouter()
router.register(r'task', views.TasksViewSet, 'tasks')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
