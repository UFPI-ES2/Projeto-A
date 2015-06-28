# -*- coding: utf-8 -*-
'''
Created on 11/05/2015

@author: Anderson
'''

from django.views.generic.edit import FormView
from daem.auth.view.LoginData import LoginData
from daem.auth.control.LoginControl import LoginControl
from daem.auth.model.LoginModel import LoginModel


class LoginView(FormView):
    """
    Classe responsável por exibir a tela de login ao usuário, fazendo a
    validação do formulário, e estabelecer a sessão caso o usuário seja
    válido.
    """
    context_object_name = "context"
    form_class = LoginData
    success_url = '/'

    def __init__(self, **kwargs):
        FormView.__init__(self, **kwargs)
        self.control = LoginControl(LoginModel())

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        code = 0
        if form.is_valid():
            lg = self.control.login(form.cleaned_data["user"],
                                    form.cleaned_data["password"])
            if lg:
                LoginView.success_url = \
                    request.GET.get("redirect_to", '/dash/')

                return self.form_valid(form)
            else:
                code = code | 4
        else:
            if form["user"].errors:
                code = code | 1
            if form["password"].errors:
                code = code | 2
        form.error_code = code
        return self.form_invalid(form)
