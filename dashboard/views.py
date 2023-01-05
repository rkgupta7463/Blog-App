from multiprocessing import context
import os
import re
from django.shortcuts import render, redirect
from django.http import *
from .models import *
# from signup.models import SignUp
from django.urls import reverse
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *

def deshboard(request):
    if request.user.is_authenticated:
        user_data = User.objects.get(username=request.user.username)
        homedata = Posts.objects.filter(author = request.user)
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()

        data = {
            'post': homedata,
            'usser_data': user_data,
            'full_name':full_name,
            'group':gps
        }
        return render(request, "desh/deshboard.html", data)
    else:
        return redirect("login")

def delete(request, id):
    if request.user.is_authenticated:
        # if request.method == 'POST':
        member = Posts.objects.get(id=id)
        member.delete()
        messages.success(request, "Blog has deleted!!")
        return redirect("deshboad")
    else:
        return redirect("login")

def update(request, id):
    if request.user.is_authenticated:
        HF = Posts.objects.get(id=id)
        if request.method == 'POST':
            if len(request.FILES) != 0:
                if len(HF.image) > 0:
                    os.remove(HF.image.path)
                HF.image = request.FILES['image_topic']
            Title = request.POST.get('title')
            Discrption = request.POST.get('discription')
            myfile1 = request.FILES['image_topic']
            fs = FileSystemStorage()
            fs.save(myfile1.name, myfile1)
            member = Posts.objects.get(id=id)
            HF.title = Title
            HF.discription = Discrption
            HF.save()
            messages.success(request, "Blog has updated!!")
            return redirect('deshboad')
        context = {
            'HF': HF,
        }
        return render(request, "desh/update.html", context)
    else:
        return redirect("login")

# add function
def AddFun(request):
    if request.user.is_authenticated:
        fm=PostForm()
        if request.method == 'POST':
            fm = PostForm(request.POST, request.FILES)
            # Get the posted form
            if fm.is_valid():
                fm.save()
                messages.success(request, "Blog has created!!")
                return redirect('deshboad')
        else:
            return render(request, "desh/add.html",{'form': fm})
    else:
        return redirect("login")

#profile Edit function
def profileEdit(request,pk):
    if request.user.is_authenticated:
        pi=User.objects.get(id=pk)
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfile(request.POST, instance=pi)
            else:
                fm = user_profile_change(request.POST, instance=pi)
            if fm.is_valid():
                messages.success(request, "Profile has updated!!")
                fm.save()
                return redirect("deshboad")
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfile(instance=pi)
            else:
                fm = user_profile_change(instance=pi)
        context = {'form': fm, }
        return render(request, "desh/profileEdit.html", context)
    else:
        return redirect("home")

#about function
def aboutus(request):
    return render(request, "desh/about.html")
