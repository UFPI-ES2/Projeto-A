'''
Created on 25/06/2015

@author: Anderson
'''
from django.conf.urls import url
from daem.doc.view.CreateDocumentView import CreateDocumentView
from daem.doc.view.ConfirmDataDocumentView import ConfirmDataDocumentView
from daem.doc.view.VisualizarDocumentos import ListDocumentsView


urlpatterns = [
    url(r"^doc/create/$",
        CreateDocumentView.as_view(),
        name="register_document"),
    url(r"^doc/create/confirm/(?P<file_id>\d+)/$",
        ConfirmDataDocumentView.as_view(),
        name="confirm_registration_document"),
    url(r"^doc/list/$",
        ListDocumentsView.as_view(),
        name="list_document"),
]
