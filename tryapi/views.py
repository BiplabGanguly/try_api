from django.shortcuts import render
from api import models


def home(req):
    projects = models.Project.objects.all()
    data = {'project': projects}
    return render(req,'index.html',data)


def api_data(req, project, pid):
    api_data = models.Apidata.objects.filter(project_uuid = pid)
    project_api = {'api_data' : api_data}
    print(api_data)
    return render(req, 'api_data.html',project_api)