from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def home(request):
    return render (request,'home.html')

def Aboutus(request):
    return render (request, 'Aboutus.html')

def contact(request):
    return render(request,'contact.html')

def account(request):
    return render(request,'account.html')

def signup(request):
  return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def transactions(request):
    return render(request,'transactions.html')

def loans(request):
    return render(request,'loans.html')

