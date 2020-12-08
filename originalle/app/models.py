from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
# Create your models here.
class jobType(models.Model):
    jobtype = models.CharField(max_length=100)
    jobdescription = models.TextField(max_length=1000,null=True)
    salary = models.IntegerField(validators=[MaxValueValidator(10000000), MinValueValidator(1)])
    experince = models.IntegerField(validators=[MaxValueValidator(21), MinValueValidator(0)])
    location = models.CharField(max_length=100)
    # def __str__(self):
    #     return self.jt


class userJobTp(models.Model):
    fname = models.CharField(max_length=100,null=True)
    lname = models.CharField(max_length=100,null=True)
    dob = models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    phonenumber = models.CharField(max_length=10,null=True)
    emai = models.EmailField(max_length=100,null=True)
    workex = models.IntegerField(null=True)
    jobdes = models.CharField(max_length=100,null=True)
    resume = models.FileField()
    