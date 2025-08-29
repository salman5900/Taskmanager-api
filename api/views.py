from django.shortcuts import render
from rest_framework import viewsets, permissions
from .permissions import CanEditOrNot
from .models import Tasks
from .serializers import TaskSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated, CanEditOrNot]
    search_fields = ['title', 'description']
    ordering_fields = ['priority', 'created_at']

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)