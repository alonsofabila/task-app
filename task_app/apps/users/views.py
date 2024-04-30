from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializer import UserSerializer
from .models import User


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
