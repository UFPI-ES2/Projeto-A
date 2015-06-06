'''
Created on 11/05/2015

@author: Anderson
'''

from django.views.generic.edit import FormView
from daem.auth.view.LoginData import LoginData
from daem.auth.control.LoginControl import LoginControl
from daem.auth.model.LoginModel import LoginModel


class LoginView(FormView):
    context_object_name = "context"
    form_class = LoginData
    success_url = '.'

    def __init__(self, **kwargs):
        FormView.__init__(self, **kwargs)
        self.control = LoginControl(LoginModel())

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            lg = self.control.login(form.cleaned_data["user"],
                                    form.cleaned_data["password"])
            if lg:
                LoginView.success_url = \
                    request.GET.get("redirect_to", '/dash/')

                return self.form_valid(form)
        return self.form_invalid(form)
