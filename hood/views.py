from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *

# Create your views here.
def homm(request,id):

    biz = Business.objects.filter(neighborhood_id=id)

    post = Post.objects.all()

    return render(request,'home.html', locals())

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()

    return render(request,'signup.html',locals())

def hood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
        return redirect('location')
    else:
        form  = NeighbourHoodForm()
    return render(request,'hood.html',locals())

def location(request):
    hood = NeighbourHood.objects.all()
    return render(request,'location.html',locals())

def post(request):
    if request.method == 'POST':
        form = MakePostForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
        return redirect('home',request.user.profile.neighborhood_id.id)
    else:
        form  = MakePostForm()
    return render(request,'post.html',locals())
