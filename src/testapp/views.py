from django.shortcuts import render_to_response,render
from .models import Section
from django.http.response import Http404, HttpResponseRedirect, HttpResponse
from django.conf.urls import url

context = {'title': 'Projeto A - Engenharia de Software 2',
               'objs' : Section.objects.all(),
               'current': None,
               }

def index(request):
    template = 'pages/dashboard.html'
    return render(request, template, context)
  
# def dashboard(request):
# #     context = {'title': 'Projeto A - Engenharia de Software 2',
# #                 'objs' : Section.objects.all(),
# #                 'current': None,
# #                 }
#     template = 'home.html'
#     return render_to_response(template, context)

def page(request, app, path):
    obj = Section.objects.get(path=path, app=app)
    
#     context = {'title': 'Projeto A - Engenharia de Software 2',
#                 'objs' : Section.objects.all(),
#                 'current': obj,
#                 }
    return 