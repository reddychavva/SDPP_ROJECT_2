# model.py
from django.db import models


# from .tpm.module1 import forms


# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.IntegerField()

    class Meta:
        db_table = "Register"

class contactus(models.Model):
     firstname = models.CharField(max_length=100)
     lastname = models.CharField(max_length=100)
     email = models.EmailField(primary_key=True)
     comment = models.CharField(max_length=100)

     class Meta:
         db_table = "contactus"




from django.db import models

# Create your models here.
