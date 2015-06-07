# -*- coding:utf-8 -*-
'''
Created on 10/05/2015

@author: Anderson
'''
from django.core.exceptions import ObjectDoesNotExist

from daem.auth.models import User


class LoginModel(object):
    def get(self, user, password):
        try:
            return User.objects.get(user=user, password=password)
        except ObjectDoesNotExist:
            return None
