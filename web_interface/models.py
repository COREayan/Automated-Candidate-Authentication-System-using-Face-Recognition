from os import name
from django.db import models
from sqlalchemy import null

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True, null=True) # optional
    lastname = models.CharField(max_length=100)
    
    rollno = models.CharField(max_length=20, unique=True) # unique student identifier
    # course = models.CharField(max_length=100)
    # gender = models.CharField(max_length=100)
    # phone = models.CharField(max_length=100)
    # address = models.TextField()
    # email = models.CharField(max_length=100)
    
    image = models.ImageField(upload_to='student_images/') # mandatory at signup ideally

    created_at = models.DateTimeField(auto_now=True)
    # updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.firstname+" "+self.lastname)
    