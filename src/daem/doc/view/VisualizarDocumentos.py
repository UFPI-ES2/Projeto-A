'''
Created on Jun 29, 2015

@author: tiagodsp
'''
from django.views.generic import TemplateView
from daem.doc.models import Document
from django.shortcuts import render_to_response

class ListDocumentsView(TemplateView):
    
    def get(self, *args, **kwargs):
        
        template_name = "pages/visualizar-documentos.html"
        context = {'documentList': Document.objects.all()
                }
        
        return render_to_response(template_name, context)