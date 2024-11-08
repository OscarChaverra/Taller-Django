from django.db import models

# Create your models here.
class Games(models.Model):    
    name = models.CharField(max_length=25, null=False,blank=False,verbose_name="game name")
    description = models.CharField(max_length=100, null=False,blank=False,verbose_name="description")
    price = models.DecimalField(decimal_places=2,max_digits=10,verbose_name="game price")