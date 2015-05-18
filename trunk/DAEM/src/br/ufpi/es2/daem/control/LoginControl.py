# -*- coding:utf-8 -*-
'''
Created on 10/05/2015

@author: Anderson
'''

from br.ufpi.es2.daem.models import User


class LoginControl(object):
    session = None

    def __init__(self, model):
        """ model é o modelo!"""
        self.model = model
        self.current_user = None

        if LoginControl.session is None:
            raise Exception("Sessão Inválida")

    def login(self, user, password):
        session = LoginControl.session
        self.current_user = self.model.get(user, password)

        if session and self.current_user:
            session["br.ufpi.es2.daem::User"] = self.current_user.user
            session["br.ufpi.es2.daem::Id"] = self.current_user.id

        return self.current_user is not None

    def logout(self):
        session = LoginControl.session
        del session["br.ufpi.es2.daem::User"]

    def current(self):
        session = LoginControl.session
        user = session.get("br.ufpi.es2.daem::User")
        if session and user:
            self.current_user = User(user=user)
        else:
            self.current_user = None
        return self.current_user

    def is_logged(self):
        return self.current_user is not None
