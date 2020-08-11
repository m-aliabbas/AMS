from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.urls import reverse
from datetime import datetime
from .models import Profile
from .models import Payment
from django.contrib.auth.models import User
import pytz

import stripe
import json
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = 'sk_test_51HD7MTCkEBLtSdgkcC6374ZUHJ2YsD0WY2cTAcjUFAf0uWXmGT06H0hsKg1hytdz7JgRCED7oNjhGsAHpcfjWtUk00JZ0cbPRt'
AMOUNT=50.00
@login_required
def checkout(request):
    return render(request,'users/checkout.html')
@login_required
def charge(request):
    amount = 50
    user_id = request.user.id
    user_name= request.user.username
    if request.method == 'POST':
        print('Data:',request.POST)
        try:
            customer = stripe.Customer.create(
                #email = request.POST['email'],
                name = user_name,
                source = request.POST['stripeToken']
            )
            charge = stripe.Charge.create(
                customer = customer,
                amount = amount*100,
                currency = 'usd',
                description = 'User Subscription'

            )
    
            return redirect(reverse('success',args=[amount]))
        except stripe.error.StripeError as e:
            
            print('Message is: %s' % e.error.message)
            error_msg = "Something went wrong"
            return redirect(reverse('error',args=[error_msg]))
        except Exception as e:
            #error_msg = e.error.message
            error_msg = "Something went wrong"
            return redirect(reverse('error',args=[error_msg]))
@login_required
def successMsg(request,args):
    user=get_object_or_404(User, username=request.user.username)
    pay=Payment.objects.filter(user=request.user.id).first()
    if pay:
        amnt=pay.amount+int(args)
        
        pay_=Payment.objects.filter(user=request.user.id).update(amount=amnt)
        print(pay_)
    else:
        payment = Payment(user=user,payment_status=True)
        payment.save()
    amount = args
    return render(request,'users/success.html',{'amount':amount})
@login_required
def CardError(request,args):
    error = args
    return render(request,'users/carderror.html',{'error':'CardError','details':error})



def delete_expired_user():
    users_to_check = Profile.objects.filter(user_type=False)
    f = open("log.txt",'a')
    now_datetime= datetime.now()
    utc=pytz.UTC
    now_datetime = utc.localize(now_datetime)
    for i in users_to_check:
        if i.expire_date < now_datetime:
            userid = i.user_id
            u = User.objects.get(id = userid)
            u.delete()
            f.write("The user with id: "+str(userid)+" expired at :"+str(now_datetime)+".\n")

# Create your views here.

def HomeView(request):
    delete_expired_user()
    context = {
      'welcome_msg' : 'Welcome to Home page.',
    }
    return render(request,'users/home.html',context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} !')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f' Your account has been Updated !!!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)