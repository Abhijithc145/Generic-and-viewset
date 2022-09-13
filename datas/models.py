from django.db import models

# Create your models here.

class Person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=20)
    
class Datas(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField()    

    