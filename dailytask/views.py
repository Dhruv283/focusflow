from django.shortcuts import render 
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import random
from .models import *
from django.utils import timezone
from django.utils.timezone import localtime


# Create your views here.
def loginpage(request):
    if request.method=="POST":
        if 'name' in request.POST:
            first_name=request.POST.get("name")
            email=request.POST.get("email")
            password=request.POST.get("password")
            
            if User.objects.filter(username=email).exists():
                
                return redirect('loginpage')
            else:
                message=f"Thank you for Joining {first_name}"
                username=email
                user=User(first_name=first_name,username=email)
                user.set_password(password)
                user.save()
                send_mail(
				    "WELCOME TO FOCUSFLOW",
				    message,
				    "pateldhruv2830@gmail.com",  # Your from email
				    [email],  # Recipient email
			        )
                
        else:
            email=request.POST.get("email")
            password=request.POST.get("password")
            user=authenticate(request,username=email,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print("USER NOT FOUND")
                pass
    return render(request,"index.html")



def logoutpage(request):
    logout(request)
    return redirect('loginpage')

@login_required(login_url='loginpage')
def home(request):
    if request.method=="POST":
        user=request.user
        date=request.POST.get("date")
        taskname=request.POST.get("taskname")
        taskpriority=request.POST.get("taskpriority")
        Task.objects.create(Username=user,date=date,taskname=taskname,taskpriority=taskpriority)
    return render(request,"home.html")

@login_required(login_url='loginpage')
def today(request):
    user=request.user
    today_date = timezone.now().date()
    tasklist = Task.objects.filter(Username=user, date=today_date)
    context={"tasklist":tasklist}
    return render(request,"today.html",context)

@login_required(login_url='loginpage')
def alltask(request):
    user=request.user
    tasklist=Task.objects.filter(Username=user).order_by('-date')
    context={"tasklist":tasklist}
    return render(request,"alltask.html",context)

@login_required(login_url='loginpage')
def status(request,id):
 
    change_sta=Task.objects.get(id=id)
    change_sta.status='Completed'
    change_sta.save()
    return redirect('alltask')


@login_required(login_url='loginpage')
def delete(request,id):
 
    Task.objects.get(id=id).delete()
    return redirect('alltask')

@login_required(login_url='loginpage')
def analysis(request):
    return render(request,"analysis.html")

@login_required(login_url='loginpage')
def aboutus(request):
    return render(request,"aboutus.html")