from django.db import models
from projects.models import Project

class User(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=45)
    lname= models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=45)
    # repwd = models.CharField(max_length=45)


    # def __str__(self) -> str:
    #     return self.fname + " " + self.lname

    class Meta:
        db_table = "user"


# class Pro(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.TextField()
#     description= models.TextField()
#     technology = models.TextField()
#     member = models.TextField()
#     image = models.ImageField()

#     class Meta:
#         db_table = "add_project"    