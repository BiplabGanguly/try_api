from django.shortcuts import render, redirect
from api import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse



def home(req):
    projects = models.Project.objects.all()
    data = {'project': projects}
    return render(req,'index.html',data)


def api_data(req, project, pid):
    api_data = models.Apidata.objects.filter(project_uuid = pid)
    project_api = {'api_data' : api_data}
    return render(req, 'api_data.html',project_api)


def admin_user_login(req):
    return render(req,'userdetails.html')


def admin_user_pass(req):
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']
        
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('admin_user',user.id)
        else:
            return redirect('home')
    else:
        return redirect('home')
    
    
@login_required
def admin_user(req,uid):
    user_data = {'uid' : uid}
    return render(req,'admin.html',user_data)