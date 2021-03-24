from django.shortcuts import redirect, render
from .models import User
import mysql.connector
from operator import itemgetter
from django.contrib import messages

def index(req):
    return render(req, 'index.html')

def login(req):
    return render(req, 'login.html')

def home(req):
    if req.method == "POST":
        user = User()
        if user.objects.get(email=req.POST['email'], password=req.POST['password']):
            return render(req, 'welcome', {'user': user})
        else:
            context = {'msg': 'Invalid email or password!'}
            return render(req, 'login', context)
            

def registration(req):
    if req.method =="POST":
        user = User(fname = req.POST['fname'],
                    lname = req.POST['lname'],
                    email = req.POST['email'],
                    password = "123",
                    )
        user.save()
        return redirect('login')
    else:
        return render(req, 'registration.html')

def welcome(req):
    return render(req, 'welcome.html')