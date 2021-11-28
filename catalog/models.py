from django.db import models

# Create your models here.
class Events(models.Model):
    
    country = models.CharField( ("country"), max_length=20)
    gender = models.CharField( ("gender"), max_length=1)
    age = models.IntegerField( ("age") )
    segments = models.CharField( ("segments"), max_length=100)

    class Filters(models.Model):
    
        gender = models.CharField( ("gender"), max_length=1)
        age = models.IntegerField( ("age") )
        country = models.CharField( ("country"), max_length=20)
        segments = models.CharField( ("segments"), max_length=100)

        def __str__(self):
            return self.gender