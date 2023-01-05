from django.shortcuts import render

# Create your views here.
from urllib import request
from django.shortcuts import redirect, render
# from signup.models import *
from django.contrib.auth.models import User,Group
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def signupUser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fname=request.POST.get("first_name")
            lname=request.POST.get("last_name")
            email=request.POST.get("email")
            username=request.POST.get("username")
            password1=request.POST.get("password1")
            password2=request.POST.get("password2")

            if password1==password2:
                user=User.objects.create_user(username=username, email=email, first_name=fname,last_name=lname,password=password1)
                user.save()
                group=Group.objects.get(name="user_pre")
                user.groups.add(group)
                login(request,user)
                messages.success(request,"Congratulations you become Author!!")
                return redirect("home")
        else:
            return render(request, "authent/submit.html")
    else:
        return redirect("signup")    
    
def loginUser(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Login Successfully!!")
            return redirect("home")
        else:
            messages.warning(request,"User or password is not correct!")

    return render(request, "authent/login.html")


def logOutUser(request):
    logout(request)
    return redirect("home")
