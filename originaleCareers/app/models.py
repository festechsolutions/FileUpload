from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
# Create your models here.
class Vacancie(models.Model):
    position = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,null=True)
    salary = models.IntegerField(validators=[MaxValueValidator(10000000), MinValueValidator(1)])
    experience = models.IntegerField(validators=[MaxValueValidator(21), MinValueValidator(0)])
    location = models.CharField(max_length=100)
    # def __str__(self):
    #     return self.jt


class Candidate(models.Model):
    First_name = models.CharField(max_length=100,null=True)
    Last_name = models.CharField(max_length=100,null=True)
    DOB = models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    phonenumber = models.CharField(max_length=10,null=True)
    mail_ID = models.EmailField(max_length=100,null=True)
    experience = models.IntegerField(null=True)
    Position = models.CharField(max_length=100,null=True)
    resume = models.FileField()
    