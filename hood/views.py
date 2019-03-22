from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def homm(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')
