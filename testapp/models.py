from django.db import models

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=120, null=False, blank=True)
    page = models.CharField(max_length=120, null=False, blank=True)
    
    def __str__(self):
        return self.name