# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import UserForm
from django.shortcuts import render, render_to_response
from .models import AuthUser
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def register_form(request):
    form=UserForm()
    return render(request, 'users/register-user.html', {'form':form})

def create(request):
    args={}
    form=UserForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/users/list')
        # print "redirecting............"
        # # HttpResponseRedirect(reverse('list'))
        # redirect('list')

    else:
        pass
    args['form']=form
    return render(request, 'users/register-user.html', args)

def list(request):
    print "redirectd to list page"
    users=AuthUser.objects.all()
    return render(request, 'users/user-list.html', {'users': users})



