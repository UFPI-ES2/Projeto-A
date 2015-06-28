'''
Created on 27/06/2015

@author: Anderson
'''
from django.views.generic.edit import FormView
from django import forms
from daem.doc.view.OcrBorder import OcrBorder
from daem.doc.view.FileControl import FileControl


class ConfirmDataDocumentView(FormView):
    template_name = "pages/confirm-registration-document.html"

    def __init__(self, **kwargs):
        FormView.__init__(self, **kwargs)
        self.fc = FileControl()

    class form_class(forms.Form):
        disciplina = forms.CharField(max_length=80)
        aluno = forms.CharField(max_length=80)

    def get_initial(self):
        tex = OcrBorder().do_ocr(self.fc.get_path(self.kwargs["file_id"]))
        return {'disciplina': tex}

    def form_valid(self, form):
        print("here")
        self.fc.store(self.kwargs["file_id"])
        return FormView.form_valid(self, form)
