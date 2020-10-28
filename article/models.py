from django.db import models

# Create your models here.
#
class article(models.Model):
    #签名
    autograph = models.CharField(max_length=10,default='未知签名')
    #标题
    title = models.CharField(max_length=20,default='未知标题')
    # 标签
    label = models.CharField(max_length=10,default='未知标签')
    #作者
    author = models.CharField(max_length=10,default='')
    #时间   天
    day =  models.CharField(max_length=10,default='')
    month = models.CharField(max_length=10,default='')
    year = models.CharField(max_length=10,default='')
    #介绍
    introduce = models.CharField(max_length=500,default='')
    #内容
    content = models.CharField(max_length=1000,default='')
    #阅读
    reads = models.CharField(max_length=50,default='0')
    #回复
    reply = models.CharField(max_length=50,default='0')