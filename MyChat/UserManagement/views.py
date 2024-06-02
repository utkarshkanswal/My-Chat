from django.shortcuts import render
from rest_framework import viewsets
from UserManagement.serializers import RegisterSerializer
from UserManagement.models import User
from rest_framework.permissions import AllowAny

class RegisterView(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    http_method_names=["put"]