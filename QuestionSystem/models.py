from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    Question_types = (
    (0, 'Radio'),
    (1, 'CheckBox'),
    (2, 'Text'),
    )
    q_text=models.TextField(max_length=1500)
    q_type=models.IntegerField(choices=Question_types,default=0)
    slug=models.SlugField(blank=True)
    order=models.IntegerField(null=True)
    timestamp=models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    question= models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_text=models.CharField(max_length=1000,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
class Next(models.Model):
    question=models.ForeignKey(Question,on_delete=models.SET_NULL, null=True)
    next_question=models.IntegerField(null=True)
class Response(models.Model):
     timestamp=models.DateTimeField(auto_now_add=True)
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     question=models.ForeignKey(Question,on_delete=models.CASCADE)
     answer_text=models.CharField(max_length=2000,default='Dummy Answer')
     feed_back=models.CharField(max_length=2000,null=True)