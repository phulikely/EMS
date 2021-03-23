from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30)
    lname= models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    pwd = models.CharField(max_length=32)
    repwd = models.CharField(max_length=32)