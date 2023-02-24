from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password=models.CharField(max_length=15)
    phno = models.CharField(max_length=10)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phno = models.CharField(max_length=10)

class Donor(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password=models.CharField(max_length=15)
    phno = models.CharField(max_length=10)