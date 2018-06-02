# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.http import HttpResponse


def index(request):
    print request.__dict__
    template = loader.get_template('home/home.html')
    return HttpResponse(template.render())

