from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class product(models.Model):
     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=False)
     name = models.CharField(max_length=200 , null=True, blank=True)
     # image=models.ImageField(upload_to='images/')
     brand= models.CharField(max_length=200 , null=True, blank=True)
     catigory = models.CharField(max_length=200, null=True, blank=True)
     description=models.TextField(null=True, blank=True)
     rating=models.DecimalField(max_digits=7, decimal_places=2)
     numReviews=models.IntegerField(default=0)
     price=models.DecimalField(max_digits=7, decimal_places=2)
     countInStock=models.IntegerField(default=0)
     createdAt=models.DateTimeField(auto_now_add=True)
     _id=models.AutoField(primary_key=True, editable=False)