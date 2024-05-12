from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


# Create your views here.
class UserViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class DetailUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

