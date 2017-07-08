from django.shortcuts import render
from django.contrib import auth
# Create your views here.
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json
from weblog.models import *

def my_login_required(func):
    def _my_login_required(*args, **kwargs):
        if not args[0].user.is_authenticated():
            return render(args[0], 'login.html')
        ret = func(*args, **kwargs)
        return ret
    return _my_login_required


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')

def login(request):
    context = {}

    if request.method == 'GET':
        context['hello'] = 'Hello World!'
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        json_data = {"login":False}
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            json_data['login']=True

        return HttpResponse(json.dumps(json_data))

@my_login_required
def home(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render(request, 'home.html', context)

@my_login_required
def details(request, blog_id):
    context = {}
    context['blog'] = Blog.objects.get(id=blog_id)
    return render(request, 'details.html', context)


