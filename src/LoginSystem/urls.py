'''
Created on 09/05/2015

@author: Anderson
'''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^login/$", views.login, name='login'),
    url(r"^logout/$", views.logout, name='logout'),
    url(r"^clogin/$", views.LoginView.as_view(), name='clogin'),
    url(r"^dlslogin/$",
        views.LoginView.as_view(template_name='LoginSystem/login.html'),
        name='dlslogin'),
]
