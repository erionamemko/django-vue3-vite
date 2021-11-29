from django.db import models

# Create your models here.
class Events(models.Model):
    
    country = models.CharField( ("country"), max_length=20)
    gender = models.CharField( ("gender"), max_length=1)
    age = models.IntegerField( ("age") )
    segments = models.CharField( ("segments"), max_length=100)