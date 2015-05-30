'''
Created on 10/05/2015

@author: Anderson
'''
from br.ufpi.es2.daem.models import User
from django.core.exceptions import ObjectDoesNotExist


class LoginModel(object):
    def get(self, user, password):
        try:
            return User.objects.get(user=user, password=password)
        except ObjectDoesNotExist:
            return None
