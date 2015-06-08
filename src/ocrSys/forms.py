from django import forms

class UploadImageToOCR(forms.Form):
    name = forms.CharField(max_length=50)
    file = forms.FileField()
#     bool = forms.BooleanField

class DocumentForm(forms.Form):
    pass