from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from polls.models import Question
from polls_api.serializers import QuestionSerializer, UserSerializer
from rest_framework import status, mixins, generics, permissions
from django.contrib.auth.models import User
from polls_api.serializers import RegisterSerializer

from rest_framework import generics,permissions
from .permissions import IsOwnerOrReadOnly


# 4. Generic API View 

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    
class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class RegisterUser(generics.ListCreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()



