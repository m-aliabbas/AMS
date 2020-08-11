from django.urls import path
from QuestionSystem.api import QuestionListAPI,AnswerListAPI
from . import views

urlpatterns=[
    path('questions/',QuestionListAPI.as_view()),
    path('show/',views.ShowQuestion,name='show_question'),
    path('show/submit_response/',views.SubmitQuestion,name='submit_question'),
    path('answers/',AnswerListAPI.as_view(),name='get_answers'),
    path('getadvise/',views.StartAdvise,name='get_advise'),
    path('getadvise/post_title/',views.PostAdivseTitle,name='post_title'),
    path('advise_list/',views.AdviceTitles,name='list_advise'),
    path('advise_list/<int:args>',views.AdviceTitlesOne,name='list_advise_1'),
    path('advise_list/mockpay',views.MockPay,name='mock_pay'),
]