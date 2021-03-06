# -*- coding:utf-8 -*-
'''
Created on 10/05/2015

@author: Anderson
'''

from daem.auth.models import User


class LoginControl(object):
    """
    classe responsável por o controle dos dados.
    """
    session = None
    SESSION_NAME = "daem.auth.user"

    def __init__(self, model):
        """ model é o modelo!"""
        self.model = model
        self.current_user = None

    def login(self, user, password):
        """
        @return True se login foi bem sucedido, caso contrário, False
        """
        session = LoginControl.session
        self.current_user = self.model.get(user, password)

        if session and self.current_user:
            session[LoginControl.SESSION_NAME] = self.current_user.user

        return (self.current_user is not None)

    def logout(self):
        """
        Efetua o logout.
        """
        session = LoginControl.session
        del session[LoginControl.SESSION_NAME]

    def current(self):
        """
        @return: o usuário cuja sessão está estabelecida, se nenhum usuário
        cumprir este requisito, returna None
        """
        session = LoginControl.session
        user = session.get(LoginControl.SESSION_NAME)
        if session and user:
            self.current_user = User(user=user)
        else:
            self.current_user = None
        return self.current_user

    def is_logged(self):
        """
        @return: True se existe um usuário com sessão estabelecida,
        False caso contrário
        """
        return self.current() is not None
