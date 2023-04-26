from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
from polls.models import Question
from polls_api.serializers import QuestionSerializer
from rest_framework.response import Response


@api_view()
def question_list(request):
    question = Question.objects.all()
    serializer = QuestionSerializer(question, many=True)
    return Response(serializer.data)



