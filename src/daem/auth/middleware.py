# -*- coding:utf-8 -*-
'''
Created on 12/05/2015

@author: Anderson
'''

from django.http.response import HttpResponseRedirect

from daem.auth.control.LoginControl import LoginControl
from daem.auth.model.LoginModel import LoginModel
import re

"""
Lista que contem os padrões de urls a serem excluidas quando
for verificada se usuário está logado.
"""
TO_EXCLUDE = [
    r'/login/',
    r'/admin/.*',
]

"""
Lista que contem as urls que não devem ser redicionada de volta quando
o login for bem sucedido.
"""
NO_REDIRECT = [
    r'/',
    r'/logout/',
]


class LoginMiddleware(object):
    """
    Classe Reponável por verificar se usuário está logado,
    se sim, não faz nada, se não, é feito um redirecionamento para
    a tela de login, salvo as excessões setadas em TO_EXCLUDE.
    """
    def to_exclude(self, path):
        """
        @param path: contem o caminho a ser testado
        @return: True se o path deve ser exluido do redirecionamento
        para a tela de login, caso contrário, False é retornado.
        """
        for p in TO_EXCLUDE:
            if re.match(r"^" + p + "$", path):
                return True
        return False

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """
        Metodo sobrecarregado que é chamado pela API Django, neste método
        é feita a verificação do login e redirecionamento caso seja
        necessário, também é feita a exclusão de urls que casam com
        os padrões setados em TO_EXCLUDE
        """
        LoginControl.session = request.session
        lc = LoginControl(LoginModel())
        vget = request.path

        if (lc.current() is None) and not self.to_exclude(vget):
            url = "/login/"

            if (vget is not None) and (vget not in NO_REDIRECT):
                url += r"?" + "redirect_to=" + vget

            return HttpResponseRedirect(url)
