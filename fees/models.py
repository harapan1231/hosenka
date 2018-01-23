from django.db import models

# Create your models here.
class SearchResult(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    published = models.DateField()

