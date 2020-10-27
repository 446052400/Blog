from django.db import models

# Create your models here.

class message(models.Model):
    username =  models.CharField(max_length=20,default="匿名")
    editor_Content = models.CharField(max_length=500)
    times = models.CharField(max_length=20,default='')
    state = models.CharField(max_length=10,default='1')
