from django.db import models

# Create your models here.
class addclients(models.Model):
    firstname=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    dni=models.IntegerField(null=False)
    origin=models.CharField(max_length=250)
    destiny=models.CharField(max_length=250)
    description=models.CharField(max_length=250 ,null=True)
    datatime=models.DateField(auto_now=True)

    