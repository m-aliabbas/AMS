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


from .models import Question,Answer,Next,Response

class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra=4
    # sortable_field_name = "position"


class QuestionAdmin(nested_admin.NestedModelAdmin):
    inlines = [AnswerInline,]

admin.site.register(Question, QuestionAdmin)