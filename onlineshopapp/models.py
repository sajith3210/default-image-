from distutils.command.upload import upload
import email
from email.policy import default
from django.db import models

# Create your models here.
class register(models.Model):
    firstname=models.CharField(max_length=30)    
    lastname=models.CharField(max_length=30)
    email=models.CharField(max_length=30,default='ss@gmail.com')
    adress=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    gender=models.CharField( max_length=20)
    countrty=models.CharField(max_length=20)
    profile_image=models.ImageField(upload_to="images/",null=True,default="static/images/default male prof.jpg")

    def __str__(self):
        return self.firstname
