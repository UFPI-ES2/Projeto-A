'''
Created on 12/05/2015

@author: Anderson
'''

from br.ufpi.es2.daem.control.LoginControl import LoginControl


class LoginMiddleware(object):
    def process_request(self, request):
        LoginControl.session = request.session
