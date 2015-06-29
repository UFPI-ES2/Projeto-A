'''
Created on 27/06/2015

@author: Anderson
'''
from django.views.generic.edit import FormView
from django import forms
from daem.doc.view.OcrBorder import OcrBorder
from daem.doc.control.FileControl import FileControl
import base64
from PIL import Image


class ConfirmDataDocumentView(FormView):
    template_name = "pages/confirm-registration-document.html"
    success_url = '/'

    def __init__(self, **kwargs):
        FormView.__init__(self, **kwargs)
        self.fc = FileControl()

    class form_class(forms.Form):
        disciplina = forms.CharField(max_length=80)
        aluno = forms.CharField(max_length=80)

    def get_context_data(self, **kwargs):
        data = super(ConfirmDataDocumentView, self).get_context_data(**kwargs)
        data['img'] = self.img
        return data

    def get_initial(self):
        p = self.fc.get_path(self.kwargs["file_id"])
        imgfile = Image.open(p)
        tex = OcrBorder().do_ocr(imgfile)[0:50]

        with open(p, "rb") as fp:
            data_readed = fp.read()
        data = base64.b64encode(data_readed)
        self.img = {
            "format": imgfile.format,
            "data": data,
        }
        return {'disciplina': tex}

    def form_valid(self, form):
        print("here")
        self.fc.store(self.kwargs["file_id"])
        return FormView.form_valid(self, form)
