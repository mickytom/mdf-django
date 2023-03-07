from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import User
from django.contrib import messages
import datetime
from . models import *


def index(request):
    context = {}
    return render(request, 'index.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def agriculture(request,):
    post = Blogposter.objects.filter(category__category=pk)
    context = {'post': post, }
    return render(request, 'agriculture.html', context)

def blog(request):
    context = {}
    return render(request, 'blog.html', context)

def causes(request):
    context = {}
    return render(request, 'causes.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def event(request):
    context = {}
    return render(request, 'event.html', context)

def gallery(request):
    context = {}
    return render(request, 'gallery.html', context)

def hair(request,pk):
    post = Blogposter.objects.filter(category__category=pk)
    context = {'post': post, }
    context = {}
    return render(request, 'hair.html', context)

def hold(request):
    context = {}
    return render(request, 'hold.html', context)

def mdfprojects(request,):
    pk = 'mdf_projects'
    post = Blogposter.objects.filter(category__category=pk)
    context = {'post': post, }
    return render(request, 'mdfprojects.html', context)

def onlinelearning(request):
    pk ='online_class'
    post = Blogposter.objects.filter(category__category=pk)
    context ={'post': post,}
    return render(request, 'onlinelearning.html', context)

def outreach(request,):
    post = Blogposter.objects.filter(category__category=pk)
    context = {'post': post, }
    return render(request, 'outreach.html', context)

def ramadan(request,pk):
    post = Blogposter.objects.filter(category__category=pk)
    context = {'post': post, }
    return render(request, 'ramadan.html', context)

def singleBlog(request, pk,):
    posts = Blogposter.objects.filter(id=pk, )
    context = {'posts': posts, }
    return render(request, 'single-causes.html', context)

def singleEvent(request):
    context = {}
    return render(request, 'single-event.html', context)

def team(request):
    context = {}
    return render(request, 'team.html', context)
