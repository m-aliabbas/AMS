from django.shortcuts import render,redirect
from django_print_sql import print_sql_decorator

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponseRedirect
from users.models import Profile,Payment
from .models import Answer,Question,UserAnswer,NextAnswer,Advise
from django.shortcuts import get_list_or_404, get_object_or_404
REQUIRED_AMMOUNT=50/3
def getAnswersJSon(request):
    question_id=request.GET.get('question',None)
    print(question_id)
    data=list(Answer.objects.filter(question=question_id).values())
    return JsonResponse(data,safe=True)
# @login_required
# def ShowAdvices(request):
#     user_id=request.user.id
#     data=UserAnswer.objects.filter(user=request.user.id)
    
#     if data:
#         user_profile=get_object_or_404(Profile,user=user_id)
#         is_admin=user_profile.user_type
#         message={'data':data,'paid':False,'admin':is_admin}
#         return render(request,'suggestion.html',{'message':message})
#     else:
#         message={'Error':'Somethig Went Wrong','txt':'Something went wrong here'}
#         return render(request,'completed.html',{'message':message})
@login_required
def MockPay(request):
    user_profile=get_object_or_404(Profile,user=request.user.id)
    is_admin=user_profile.user_type
    user_=get_object_or_404(User,username=request.user.username)
    if is_admin:
        pay_,created=Payment.objects.get_or_create(user=user_,amount=100,payment_status=True)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def AdviceTitles(request):
    user_id=request.user.id
    advises=Advise.objects.filter(user=user_id)
    if advises:
        message={'title':'','txt':'','data':advises}
        return render(request,'advises_list.html',{'message':message})
    else:
        message={'title':'','txt':'Please Start Taking Advise by Answering Questions'}
        return render(request,'advises_list.html',{'message':message})
@login_required
def AdviceTitlesOne(request,args):
    user_id=request.user.id
    
    data=UserAnswer.objects.filter(user=user_id,advise=args)
    pay_stat=Advise.objects.filter(user=user_id,id=args).first()
    user_profile=get_object_or_404(Profile,user=user_id)
    is_admin=user_profile.user_type
    if data:
        if pay_stat.is_paid:
            paid=2
        else:

            pay=Payment.objects.filter(user=user_id).first()
            print(pay)
            paid=0
            if pay:
                if pay.amount>=REQUIRED_AMMOUNT:
                    amnt=float(pay.amount)-REQUIRED_AMMOUNT
                    paid=2
                    pay_=Payment.objects.filter(user=user_id).update(amount=amnt)
                    advs_=Advise.objects.filter(user=user_id,id=args).update(is_paid=True)
                else:
                    paid=1
            else:
                paid=0
        message={'data':data,'paid':paid,'admin':is_admin}
        return render(request,'suggestion.html',{'message':message})
    else:
        message={'title':'','txt':'Please Start Taking Advise by Answering Questions'}
        return render(request,'advises_list.html',{'message':message})
@login_required
def StartAdvise(request):
    user_id=request.user.id
    advise=Advise.objects.filter(user=user_id,is_completed=False).first()
    if advise:
        advise_id=advise.id
        return redirect(ShowQuestion)
    else:
        message={'title':'','txt':''}
        return render(request,'advise_form.html',{'message':message})
@login_required
def PostAdivseTitle(request):
    user_id=request.user.id
    if request.method=='POST':
        advise_title=request.POST.get('advise_title')
        user=get_object_or_404(User, username=request.user.username)
        advise=Advise(title=advise_title,user=user).save()
        return redirect(ShowQuestion)
    else:
        return redirect(ShowQuestion)
@login_required
def ShowQuestion(request):
    advise=Advise.objects.filter(user=request.user.id,is_completed=False).first()
    
    if advise:
        print(advise.id)
        user_id=request.user.id
        existing_question_id=list(UserAnswer.objects.filter(user=user_id,advise=advise.id).values('id','question').order_by('id'))
        print('Existing Question ID',existing_question_id)
        if len(existing_question_id)==0:
            question=list(Question.objects.all().values('id','q_title','q_text','q_type').order_by('id'))[0]
            answers=list(Answer.objects.filter(question=question['id']).values('id','answer_text'))
        if len(existing_question_id)>0:
            print('Len',len(existing_question_id)-1)
            ex_question=get_object_or_404(Question,id=existing_question_id[len(existing_question_id)-1]['question'])
            user_ans=UserAnswer.objects.filter(question=ex_question.id,advise=advise.id).first()
            # print(existing_question_id,user_ans)
            quiz_completed=user_ans.user_response.exit_quiz
            if quiz_completed:
                data=UserAnswer.objects.filter(user=request.user.id,advise=advise.id)
                Advise.objects.filter(pk=advise.id).update(is_completed=True)
                message={'title':'Questions Completed','txt':'Questionaries Completed. Please Vist Advise Center to Reterive your message'}
                return render(request,'completed.html',{'message':message})
            print(user_ans.question.q_text,user_ans.user_response.answer_text)
            next_q=NextAnswer.objects.filter(question=user_ans.question.id,answer=user_ans.user_response.id).first()
            print(next_q,user_ans.question.id,user_ans.user_response.id)
            if next_q:
                next_q_id=next_q.next_question.id
                print(next_q_id)
                question=Question.objects.filter(id=next_q_id).values('id','q_title','q_text','q_type').order_by('id').first()
            else:
                print('Not Feild')
                question=Question.objects.filter(id__gt=ex_question.id).values('id','q_title','q_text','q_type').order_by('id').first()
            if question:
                answers=list(Answer.objects.filter(question=question['id']).values('id','answer_text'))
            else:
                message={'Error':'Somethig Went Wrong','txt':'Something went wrong here'}
                return render(request,'completed.html',{'message':message})
        return render(request,'question.html',{'question':question,'answer':answers})
    else:
        return redirect(StartAdvise)
   
    
    # if len(existing_question_id)>0:
        # question=list(Question.get_next_by_number(issue, ))

@login_required
def SubmitQuestion(request):
    if request.method=='POST':
        if len(request.POST.getlist('user_response')):
            user_responses=request.POST.getlist('user_response')
            advise_id=list(Advise.objects.filter(user=request.user.id,is_completed=False).values('id'))
            print(advise_id)
            for i,j in enumerate(user_responses):
                answer_data=list(Answer.objects.filter(id=user_responses[i]).values('question','response','response_part'))
                question=get_object_or_404(Question,pk=answer_data[0]['question'])
                answer=get_object_or_404(Answer,pk=user_responses[i])
                user=get_object_or_404(User, username=request.user.username)
                advise=get_object_or_404(Advise,pk=advise_id[0]['id'])
                print(question,answer)
                useranswer=UserAnswer(question=question,user=user,user_response=answer,suggestion=answer_data[0]['response_part'],suggestion_gen=answer_data[0]['response'],advise=advise)
                
                useranswer.save()
            # if request.POST.get('user_response'):
            # #     user_response=request.POST.get('user_response')
            # print(request.POST.getlist('user_response'))
            #     # question_id=Answer.objects.filter(id=user_response)
        return redirect(ShowQuestion)
    # if request.method == 'GET':
    #     # print(request.POST)
    #     return render(request, 'question.html') 
