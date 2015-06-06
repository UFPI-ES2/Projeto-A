'''
Created on 12/05/2015

@author: Anderson
'''

from django.http.response import HttpResponseRedirect

from daem.auth.control.LoginControl import LoginControl
from daem.auth.model.LoginModel import LoginModel
import re

TO_EXCLUDE = [
    r'/login/',
    r'/admin/.*',
]

NO_REDIRECT = [
    r'/',
    r'/logout/',
]


class LoginMiddleware(object):
    def to_exclude(self, path):
        for p in TO_EXCLUDE:
            if re.match(r"^" + p + "$", path):
                return True
        return False

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        LoginControl.session = request.session
        lc = LoginControl(LoginModel())
        vget = request.path

        if (lc.current() is None) and not self.to_exclude(vget):
            url = "/login/"

            if (vget is not None) and (vget not in NO_REDIRECT):
                url += r"?" + "redirect_to=" + vget

            return HttpResponseRedirect(url)
