from django.db import models
from .category import Category

# Create your models here.
class St(models.Model):
    name=models.CharField(max_length=30)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    profileimg=models.ImageField(upload_to='img')
    regdno=models.CharField(max_length=20)
    fee=models.IntegerField()