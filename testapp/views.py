from django.shortcuts import render_to_response
from .models import Section
from django.http.response import Http404

def index(request):
    context = {'title': 'Projeto A - Engenharia de Software 2',
               'objs' : Section.objects.all(),
               'current': None,
               }
    template = 'home.html'
    return render_to_response(template, context)
  
def dashboard(request):
    context = {'title': 'Projeto A - Engenharia de Software 2',
                'objs' : Section.objects.all(),
                'current': None,
                }
    template = 'home.html'
    return render_to_response(template, context)

def page(request, path):
    obj = Section.objects.get(path=path)
    context = {'title': 'Projeto A - Engenharia de Software 2',
                'objs' : Section.objects.all(),
                'current': obj,
                }
    return render_to_response(obj.page, context)