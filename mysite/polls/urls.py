from django.urls import path
from . import views

app_name = 'questions'
urlpatterns = [
    path("", views.index, name="index"),
    path('<int:question_id>/', views.detail, name='question_detail'),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('<int:question_id>/result', views.result, name='result'),
    
    #path('', include('polls.url', name='polls'))
]
