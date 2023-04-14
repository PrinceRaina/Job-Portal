from django.db import models

# Create your models here.
class signup(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    Mobile=models.IntegerField(max_length=10)
    Otp=models.IntegerField(max_length=4)

class login(models.Model):
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)    