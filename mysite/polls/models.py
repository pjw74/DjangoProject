from django.db import models

# Create your models here.
# 모델 생성
# 모델을 테이블에 써 주기 위한 마이그레이션이라는걸 만든다.
# 이 모델에 맞는 테이블을 만듭니다.
# 질문: 여름에 놀러간다면 어디에 갈래?
# 산
# 강
# 바다
# 도심 호캉스


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    # score = models.FloatField(default=0)
    # is_something_wrong = models.BooleanField(default=False)
    # json_field = models.JSONField(default=dict)

    def __str__(self):
        return f"제목: {self.question_text}, 날짜: {self.pub_date}"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
