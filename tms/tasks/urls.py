from django.conf.urls import url
from views import *

urlpatterns=[
    url(r'$',  create_tasks)
]