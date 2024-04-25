from django.urls import path, include
from rest_framework import routers
from task_app.apps.users import views


# Api versioning
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, 'users')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
