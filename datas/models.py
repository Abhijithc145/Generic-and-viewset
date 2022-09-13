from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=20)

class Datas(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField()    


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.PositiveIntegerField(max_length=20)
    batch = models.CharField(max_length=100)


class Valus(models.Model): 
    value1= models.PositiveIntegerField(max_length=100)
    value2 = models.PositiveIntegerField(max_length=20)
    value3 = models.PositiveIntegerField(max_length=100)
   
