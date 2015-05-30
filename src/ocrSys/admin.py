from django.contrib import admin
from .models import Document

# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title','discipline','professor')
#     self.fieldsets = 
admin.site.register(Document, DocumentAdmin)