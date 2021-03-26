from django.shortcuts import redirect, render, HttpResponseRedirect
from .models import User


def index(req):
    return render(req, 'index.html')


def login(req):
    return render(req, 'login.html')


def project(req):
    print('bbbbbb')
    if req.method == "POST":
        if User.objects.filter(email=req.POST['email'], password=req.POST['password']).exists():
            print('aaaaaaaaaaaaaaaaaa')
            user = User.objects.get(email=req.POST['email'], password=req.POST['password'])
            return render(req, 'project_index.html', {'user': user})
            #return redirect('welcome', {'user': user})
        else:
            context = {'msg': 'Invalid email or password!'}
            return render(req, 'login.html', context)
            

def registration(req):
    if req.method =="POST":
        # Check email exists or not
        if User.objects.filter(email=req.POST['email']).exists():
            context = {'msg': 'Email already existed!'}
            return render(req, 'registration.html', context)
        # Check password matching        
        elif req.POST['pwd'] != req.POST['repwd']:
            context = {'msg': 'Passwords do not match!'}
            return render(req, 'registration.html', context)           
        user = User(fname = req.POST['fname'],
                    lname = req.POST['lname'],
                    email = req.POST['email'],
                    password = req.POST['pwd'],
                    )
        user.save()
        return redirect('login')
    else:
        return render(req, 'registration.html')