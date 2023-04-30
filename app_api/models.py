from django.db import models

# Create your models here.


class Users(models.Model):
    name= models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    password=models.CharField(max_length=10)
