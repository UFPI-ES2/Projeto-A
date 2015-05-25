from django.shortcuts import render, render_to_response
from django.views.generic.edit import FormView
from .forms import UploadImageToOCR
from .controllers.OCR import OCR
from .models import Document
# class OCRFormView(FormView):
#     context_object_name = "context"
#     form_class = UploadImageToOCR
#     template_name = 'scan_document.html'
#     success_url = './'

def scan_document_form(request):
    template = 'scan_document.html'
    if(request.method == 'POST'):
#         print('IMG TO OCR:'+request.FILES.get('image'))
        form = UploadImageToOCR(request.POST, request.FILES)
        print(request.FILES)
        print(request.POST)
        handle_uploaded_file(request.FILES['file'])
        txt = OCR().scanImage('./file')
        return render(request,template, {'form':form, 'ocr_data': txt})
        
    else:
        form = UploadImageToOCR()
#     print("FORMULARIO:"+form)
    return render(request,template, {'form':form})

def handle_uploaded_file(f):
    with open('./file', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
