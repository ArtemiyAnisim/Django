from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

import socket
import os

def home(request):
    host = socket.gethostname()
    browser = request.META['HTTP_USER_AGENT']
    ip = request.META['REMOTE_ADDR']
    return render(request, 'home.html', {'host': host, 'browser': browser, 'ip': ip})

def error(request):
    return HttpResponse('К сожалению произошла ошибка', status=500)

def user(request, login='default_login', folder='default_folder', post_num='default_post_num'):
    return render(request, 'user.html', {'login': login, 'folder': folder, 'post_num': post_num})
