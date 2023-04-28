from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from polls.models import Question,Choice, Vote
from polls_api.serializers import QuestionSerializer, UserSerializer, RegisterSerializer, VoteSerializer
from rest_framework import status, mixins, generics, permissions
from django.contrib.auth.models import User

from rest_framework import generics,permissions
from .permissions import IsOwnerOrReadOnly, IsVoter

from rest_framework import status
from rest_framework.response import Response

class VoteList(generics.ListCreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Vote.objects.filter(voter=self.request.user) # 나만 볼 수 있게

    def create(self, request, *args, **kwargs):
        new_data = request.data.copy()
        new_data['voter'] = request.user.id
        serializer = self.get_serializer(data=new_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsVoter]
    
    def perform_update(self, serializer):
        serializer.save(voter=self.request.user)
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



