from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from django.dispatch import receiver
from django.utils.timezone import now
# Create your models here.

class Question(models.Model):
    Question_types = (
    (0, 'Radio'),
    (1, 'CheckBox'),
    (2, 'Text'),
    )
    q_title=models.CharField(max_length=100)
    q_text=models.TextField(max_length=1500)
    q_type=models.IntegerField(choices=Question_types,default=0)
    slug=models.SlugField(blank=True)
    order=models.IntegerField(null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return self.q_title
class Answer(models.Model):
    question= models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_text=models.CharField(max_length=1000,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    exit_quiz=models.BooleanField(default=False)
    response=models.TextField(max_length=1500,null=True,blank=True) 
    response_part=models.TextField(max_length=1500,null=True,blank=True) 
    def __str__ (self):
        return self.answer_text
class NextAnswer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    next_question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='%(class)s_requests_created')
    timestamp=models.DateTimeField(auto_now_add=True)
class Advise(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200,default=now,editable=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    is_completed=models.BooleanField(default=False)
    is_paid=models.BooleanField(default=False)
    def __str__ (self):
        return self.title
class UserAnswer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    advise=models.ForeignKey(Advise,on_delete=models.CASCADE,default=1)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    user_response=models.ForeignKey(Answer,on_delete=models.CASCADE)
    suggestion=models.TextField(max_length=1500,null=True,blank=True)
    suggestion_gen=models.TextField(max_length=1500,null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)


@receiver(pre_save,sender=Question)
def slugify_name(sender,instance,*args,**kwargs):
    instance.slug=slugify(instance.q_title)
