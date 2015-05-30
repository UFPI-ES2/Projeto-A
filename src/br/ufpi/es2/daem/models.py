'''
Created on 11/05/2015

@author: Anderson
'''
from django.db import models


class User(models.Model):
    user = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.user
