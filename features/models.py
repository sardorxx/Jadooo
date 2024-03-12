from django.db import models
from uuid import uuid4


# Create your models here.


class QuestionAnswer(models.Model):
    question_id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)
    question_text = models.CharField(max_length=100, unique=True)
    answer_text = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media/answer/', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


class News(models.Model):
    news_id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)
    text = models.TextField(max_length=500)
    image = models.ImageField(upload_to='media/news/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
