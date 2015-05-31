from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic.base import View

from br.ufpi.es2.daem.control.LoginControl import LoginControl
from br.ufpi.es2.daem.model.LoginModel import LoginModel
from br.ufpi.es2.daem.view.LoginView import LoginView
from br.ufpi.es2.daem.view.LoginData import LoginData

control = LoginControl(LoginModel())


# Create your views here.
def login(request):
    print("hher")
    form = LoginData()
    print(form)
    print(render_to_response('LoginSystem/login.html', context={"form": form}))
    return render_to_response('LoginSystem/login.html', context={"form": form})


def logout(request):
    control.logout()
    return HttpResponseRedirect(reverse('index'))


def index(request, **kwargs):
    current = control.current()
    if current is not None:
        ret = render_to_response(template_name='index.htm',
                                 context={"current": current})
#         ret.set_cookie("redirect_to", "home.html")
        return ret
    else:
        print(reverse('dlslogin'))
        return HttpResponseRedirect(reverse('dlslogin'))
