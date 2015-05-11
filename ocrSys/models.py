from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    discipline = models.CharField(max_length=120, null=True, blank=True)
    professor = models.CharField(max_length=120, null=True, blank=True)
    def __str__(self):
        return self.title