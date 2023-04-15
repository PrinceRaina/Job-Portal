from django.db import models

# Create your models here.
class signup(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
    mobile=models.IntegerField(max_length=10,null=True)
    otp=models.IntegerField(max_length=4,null=True)

class login(models.Model):
    email=models.EmailField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)    