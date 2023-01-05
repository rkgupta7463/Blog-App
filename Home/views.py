from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from dashboard.models import *
import os
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

# @login_required
def Home(request):
    # if request.user.is_authenticated:
        post=Posts.objects.all()
        paginator = Paginator(post, 10)
        page_numer = request.GET.get('page')
        BlogDatafinal = paginator.get_page(page_numer)
        totalpage = BlogDatafinal.paginator.num_pages

        context={
            'post':BlogDatafinal ,
            'lastpage': totalpage,
            'totalpagelist': [n+1 for n in range(totalpage)],
        }

        return render(request, "main/home.html",context)
    # else:
    #     return redirect("login")
#contact function 
def ContactForm(request):
    # if request.user.is_authenticated:
        if request.method=="POST":
            fm=ContactFm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,"Thank for contacting us about bloging!! Our team will contact soon to you")
                if request.user.is_authenticated:
                    return HttpResponseRedirect("/deshboad/deshboad/")
                else:
                    return redirect("home")    
        else:
            fm=ContactFm()
        return render(request, "main/contact.html",{'form':fm})
    # else:
    #     return redirect("login")