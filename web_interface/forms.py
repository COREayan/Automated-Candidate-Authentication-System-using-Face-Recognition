from calendar import c
from django.db import models  
from django.forms import fields  
from .models import Student 
from django import forms  
  


'''gender_choices= [
    ('NA', 'Select any one'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
    ]

course_choices= [
    ('NA', 'Select any one'),
    ('B.Tech', 'B.Tech'),
    ('BCA', 'BCA'),
    ('BBA', 'BBA'),
    ('M.Tech', 'M.Tech'),
    ('MCA','MCA'),
    ('MBA','MBA'),
    ]'''
  
class StudentSignupForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = Student  
        # It includes all the fields of model  
        fields = ('firstname', 'middlename', 'lastname', 'rollno', 'image')

        labels = {
        }

        widgets = {
            'firstname' : forms.TextInput(attrs= {'class': 'inp', 'id': 'firstname', 'placeholder':'Enter Firstname'}),
            'middlename' : forms.TextInput(attrs= {'class': 'inp', 'id': 'middlename', 'placeholder':'Enter Middlename'}),
            'lastname' : forms.TextInput(attrs= {'class': 'inp', 'id': 'lastname', 'placeholder':'Enter Lastname'}),
            'rollno' : forms.TextInput(attrs= {'class': 'inp', 'id': 'rollno', 'placeholder':'Enter Roll Number'}),
        }