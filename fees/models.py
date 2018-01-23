from django.db import models

# Create your models here.
class SearchResult(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    published = models.DateField()

class Totaling(models.Model):
    ins_id = models.CharField(max_length=12)
    history = models.IntegerField
    amount_fee = models.DecimalField(max_digits=8, decimal_places=0)

