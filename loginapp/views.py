from django.shortcuts import render

def welcome(req):
    return render(req, 'welcome.html')

def login(req):
    return render(req, 'login.html')

def registration(req):
    return render(req, 'registration.html')