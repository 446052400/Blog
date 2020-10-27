from django.db import models

# Create your models here.

class diary(models.Model):
    year = models.CharField(max_length=20,default="")
    data = models.CharField(max_length=20,default='')
    my_message= models.CharField(max_length=50,default='')