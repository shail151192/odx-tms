# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import UserForm
from django.shortcuts import render
from .models import AuthUser
from django.http import HttpResponse, HttpResponseRedirect

def register_form(request):
    form=UserForm()
    return render(request, 'users/register-user.html', {'form':form})

def create(request):
    args={}
    form=UserForm(request.POST)
    if form.is_valid():
        form.save()
        HttpResponseRedirect('/users/list')
    else:
        pass
    args['form']=form
    return render(request, 'users/register-user.html', args)

def list(request):
    users=AuthUser.objects.all()
    return render(request, 'users/user-list.html', {'users': users})



