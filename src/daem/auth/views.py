from django.http.response import HttpResponseRedirect

from daem.auth.control.LoginControl import LoginControl
from daem.auth.model.LoginModel import LoginModel


# from django.views.generic.base import View
control = LoginControl(LoginModel())


def logout(request):
    control.logout()
    return HttpResponseRedirect('/login/')


def index(request, **kwargs):
    current = control.current()
    if current is not None:
        ret = HttpResponseRedirect('/dash/')
        return ret
    else:
        return HttpResponseRedirect('/login/')
