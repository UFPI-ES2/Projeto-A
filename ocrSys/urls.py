from django.conf.urls import url
from . import views

urlpatterns = [
#                url(r'^$', views.index, name='index'),
               url(r'^upload', views.scan_document_form, name='upload'),
               ]