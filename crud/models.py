from django.db import models


# Create your models here.
class Students(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30, default="")
    lname = models.CharField(max_length=30, default="")


class Myusers(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, default="")
    email = models.CharField(max_length=254, default="",unique=True)
    password = models.CharField(max_length=30, default="")
    join_date = models.DateField()
    login_time = models.TimeField()
    is_login = models.BooleanField(default=False)
