from django.urls import path, include
from .views import *

urlpatterns = [
    path('question/', QuestionList.as_view(), name='question-list'),
    path('question/<int:pk>/', QuestionDetail.as_view()),
    path('users/', UserList.as_view(),name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('register/', RegisterUser.as_view()),
    path('api-auth/', include('rest_framework.urls'))
    
    
    
    
    
    #path('signup/', SignView.as_view(), name='signup'),
    #path('api-auth/', include('rest_framework.urls')),    
    #2. path('question/<int:id>/', QuestionDetail.as_view(), name='question-detail'),
    #1. path('question/<int:id>/', question_detail, name='question-detail'),
    
]


