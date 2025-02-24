from os import name
from django.db import models
from sqlalchemy import null

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    rollno = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    email = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null = True, upload_to='images/')

    def __str__(self):
        return str(self.firstname+" "+self.lastname)
    