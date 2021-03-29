from django.shortcuts import redirect, render
from .models import User
from projects.views import project_detail, project_index
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from projects.models import Project

def index(req):
    return render(req, 'index.html')


def login(req):
    return render(req, 'login.html')


def add_project(req):
    return render(req, 'add_project.html')


def add(req):
    if req.method == "POST" and req.FILES['btn_img']:
        myfile = req.FILES['btn_img']
        fs = FileSystemStorage()
        print(myfile)

        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)


        pro = Project(title=req.POST['project_title'],
                    description=req.POST['project_description'],
                    technology=req.POST['project_technology'],
                    member=req.POST['project_member'],
                    image=f"img/{filename}",
                    )
        pro.save()
        return redirect('login')
    else:
        return render(req, 'add_project.html')

def project(req):
    if req.method == "POST":
        if User.objects.filter(email=req.POST['email'], password=req.POST['password']).exists():
            user = User.objects.get(email=req.POST['email'], password=req.POST['password'])
            return project_index(req)
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