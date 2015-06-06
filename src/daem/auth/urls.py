'''
Created on 09/05/2015

@author: Anderson
'''
from django.conf.urls import url
from . import views
from .view.LoginView import LoginView

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^logout/$", views.logout, name='logout'),
    url(r"^login/$",
        LoginView.as_view(template_name='daem.auth/login.html'),
        name='login'),
]
