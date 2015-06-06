from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import User


class UserAdmin(ModelAdmin):
    list_display = ('id', 'user')
    fieldsets = [
                 ('Section Name', {'fields': ['user', 'password']}),
                 ]


admin.site.register(User, UserAdmin)
