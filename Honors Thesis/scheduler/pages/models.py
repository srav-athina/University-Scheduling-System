from django.db import models
import json

#username = admin
#password = husky2023
# Create your models here. - represent tables in database

class Course(models.Model):
    dept = models.CharField(max_length = 50)
    number = models.CharField(max_length = 50)
    name = models.CharField(max_length = 100)
    credits = models.CharField(max_length = 50)
    dependencies = models.ManyToManyField("self", verbose_name="list of dependencies")

class Prof(models.Model):
    name = models.CharField(max_length = 100)
    courses = models.ManyToManyField(Course, verbose_name="list of eligible courses")
    hard_times = models.CharField(max_length = 500)
    soft_times =  models.CharField(max_length = 500)
    profID = models.CharField(max_length = 100)
    
class Room(models.Model):
    location = models.CharField(max_length = 100)
    number = models.CharField(max_length = 50)
