# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from users.models import AuthUser
from django.http import HttpResponseRedirect
# Create your views here.
def login_view(request):
    if request.method=='GET':
        return render(request, 'login/login.html', {})

    elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print username, password
        user=authenticate(request,username=username, password=password)
        print user
        if user:
            login(request,user)
            print "user successfully authenticated"
            return HttpResponseRedirect('/users/list')

        else:
            print "user not authenticated"
            return render(request, 'login/login.html', {})


def logout_view(request):
    pass