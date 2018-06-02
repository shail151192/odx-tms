from django.conf.urls import *
from .views import *

urlpatterns=[(
    url(r'^$', login_view, name='login_view')
)]