# -*- coding:utf-8 -*-
'''
Created on 10/05/2015

@author: Anderson
'''
from django import forms


class LoginData(forms.Form):
    user = forms.CharField(label='Usuário',
                           widget=forms.TextInput)
    password = forms.CharField(label='Senha',
                               widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginData, self).clean()
        user = cleaned_data.get('user')
        password = cleaned_data.get('password')

        if (not user or not password):
            raise forms.ValidationError("User or Password is empty")

        return cleaned_data
