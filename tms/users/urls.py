from django.conf.urls import url
from .views import *

urlpatterns=[
    url(r'^register/$', register_form, name='register'),
    url(r'^create/$', create, name='create'),
    url(r'^list', list, name='list')

]