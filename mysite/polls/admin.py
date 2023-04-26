from django.contrib import admin
from .models import *


# CRUD Create Read Update Delete

# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3
class ChoiceInline(admin.TabularInline): # choice와 votes 같은 줄로 만들고 싶을 때
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('질문 섹션', {'fields': ['question_text']}),   
        ('생성일', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text','pub_date','was_published_recently')
    readonly_fields = ['pub_date']
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text','choice__choice_text']
    
admin.site.register(Question, QuestionAdmin)
