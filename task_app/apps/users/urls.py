from django.urls import path, include
from task_app.apps.users.views import UserViewSet, DetailUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('api/v1/user/register/', UserViewSet.as_view(), name="register"),
    path('api/v1/user/<int:pk>/', DetailUserView.as_view(), name="user"),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/api-auth/', include('rest_framework.urls')),
]
