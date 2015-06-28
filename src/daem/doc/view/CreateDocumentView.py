'''
Created on 25/06/2015

@author: Anderson
'''
from django.views.generic.edit import FormView
from django import forms
from django.core.urlresolvers import reverse
from daem.doc.view.FileControl import FileControl


class CreateDocumentView(FormView):
    class form_class(forms.Form):
        image = forms.FileField()

    success_url = "/doc/create/confirm/"
    template_name = "pages/cadastrar-document.html"

    def form_valid(self, form):
        fc = FileControl()
        imgfile = form.cleaned_data["image"]
        file_id = fc.save(imgfile)

        self.success_url = reverse("confirm_registration_document",
                                   kwargs={"file_id": file_id})

        return FormView.form_valid(self, form)
