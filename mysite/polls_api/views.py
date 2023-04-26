from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from polls.models import Question
from polls_api.serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.views import APIView





# 4. Generic API View 

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    
class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer



# 3. Mixin 활용
"""
class QuestionList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    def get(self, request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self, request, *args,**kwargs):
        return self.create(request,*args,**kwargs)

class QuestionDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""    

    
    
    

# 2. Class 기반의 뷰로 구현하기

"""
class QuestionList(APIView):
    def get(self, request):
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):
    def get(self, request, id):
        question = get_object_or_404(Question, pk=id)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    
    def put(self, request, id):
        question = get_object_or_404(Question, pk=id)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        question = get_object_or_404(Question, pk=id)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
        

        

# 1. 함수화 전

"""
@api_view(['GET','POST'])
def question_list(request):
    if request.method == 'GET':
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            
            
@api_view(['GET','PUT','DELETE'])    
def question_detail(request, id):
    question = get_object_or_404(Question, pk=id)
    
    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     
"""   



