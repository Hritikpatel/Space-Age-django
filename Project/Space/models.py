from django.db import models

# Create your models here.
class login(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=18)
class personalinfo(models.Model):
    fullname = models.CharField(max_length=255)
    gender= models.CharField(max_length=255)
    email= models.EmailField(max_length=50)
    phn_no = models.IntegerField()
    address = models.TextField(max_length = 255)
    emergency_number= models.CharField(max_length=50)
    gov_id = models.CharField(max_length = 16)

class booking(models.Model):
    date = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    User_id = models.CharField(max_length=50)
    name = models.CharField(max_length=25)
    contactinfo = models.CharField(max_length=25,)
    pkgname = models.CharField(max_length=255)
    level = models.CharField(max_length=50)
    tripstatus = models.IntegerField(default=0) # 1 for scheduled,2 for completed
    trans_id = models.CharField(max_length=50)
    cost =  models.CharField(max_length=50)
class blogpost(models.Model):
    title = models.TextField(max_length = 100)
    body = models.TextField(max_length = 1000)
    username = models.TextField(max_length = 30, default ="")