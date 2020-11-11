from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import LogInSerializer, UserSerializer, ProfileSerializer



class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class LogInView(TokenObtainPairView):
    serializer_class = LogInSerializer

class ProfileView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return get_user_model().objects.filter(username=self.request.user.username)
    