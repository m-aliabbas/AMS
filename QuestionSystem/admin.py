# from django.contrib import admin
# from .models import Question,Answer,Next,Response
# import nested_admin
# class AnswerInline(nested_admin.NestedTabularInline):
#     model=Answer
#     extra=4
#     max_num=4
# class QuestionInline(nested_admin.NestedTabularInline):
#     model=Question
#     inlines=[AnswerInline,]
#     extra=5
# class QuestionAdmin(nested_admin.NestedModelAdmin):
#     ilines=[QuestionInline,]

# admin.site.register(Question,QuestionAdmin)

# admin.site.register(Answer)
# admin.site.register(Next)
# admin.site.register(Response)
from django.contrib import admin
import nested_admin

from django import forms
from .models import Question,Answer,NextAnswer

class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra=4
    # sortable_field_name = "position"


class QuestionAdmin(nested_admin.NestedModelAdmin):
    inlines = [AnswerInline,]

class AuthorForm(forms.ModelForm):
    
    question = forms.ModelChoiceField(queryset=Question.objects.all())
    answer=forms.ModelChoiceField(queryset=Answer.objects.all())
    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.fields['question'].widget.attrs\
            .update({
                'id':'question_id_field'
            })
        self.fields['answer'].widget.attrs\
            .update({
                'id':'answer_id_field'
            })
class NextQuestionAdmin(admin.ModelAdmin):
    class Media:
        js = ['choice.js']
    form=AuthorForm
    
    change_form_template='admin/NextQuestion/NextQuestion.html'
admin.site.register(Question, QuestionAdmin)
admin.site.register(NextAnswer,NextQuestionAdmin)