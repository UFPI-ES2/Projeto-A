from django.conf.urls import url, include
from . import views

urlpatterns = [
               url(r'^$', views.index, name='index'),
#                url(r'^dashboard/$', views.dashboard, name='dashboard'),
#                 url(r'^', views.index, name='dashsection'),
                url(r'^ocr/', include('ocrSys.urls')),
                url(r'^(?P<app>\w*)/(?P<path>\w*)/$', views.page , name='dashsection'),
               ]