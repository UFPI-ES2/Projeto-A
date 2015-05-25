from django.contrib import admin
from .models import Section
# Register your models here.
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name','app','path','page')
    fieldsets = [
                 ('Section Name',{'fields': ['name','app','path','page']}),
                 ]
#     class Meta:
#         model = Section
        
admin.site.register(Section, SectionAdmin)