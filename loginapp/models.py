from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=45)
    lname= models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=45)
    # repwd = models.CharField(max_length=45)


    def __str__(self) -> str:
        return self.fname + " " + self.lname

    class Meta:
        db_table = "user"