from django.db import models

# Create your models here.
class FilesUpload(models.Model):
	fname=models.CharField(max_length=100,null=True)
	lname=models.CharField(max_length=100,null=True)
	phonenumber=models.CharField(max_length=10,null=True)
	emai=models.EmailField(max_length=100,null=True)
	workex=models.IntegerField(null=True)
	jobdes=models.CharField(max_length=1000,null=True)
	file = models.FileField()