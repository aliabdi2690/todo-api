from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView 
from rest_framework import viewsets
from .serializers import todo_serializer
from .models import todolist
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated

class todolistview(viewsets.ModelViewSet):
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = todo_serializer
    def get_queryset(self):
        return todolist.objects.filter(owner=self.request.user)

    
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)