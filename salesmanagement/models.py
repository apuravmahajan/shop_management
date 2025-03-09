from django.db import models

# Create your models here.
class salesData(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    cp = models.FloatField()
    sp = models.FloatField()
    profit = models.FloatField()