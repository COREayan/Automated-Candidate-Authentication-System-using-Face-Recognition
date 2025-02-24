from calendar import c
from django.db import models  
from django.forms import fields  
from .models import Student 
from django import forms  
  


gender_choices= [
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
    ]
  
class UserImageForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = Student  
        # It includes all the fields of model  
        fields = ('firstname', 'middlename', 'lastname', 'rollno', 'course', 'gender', 'phone', 'address', 'email', 'image')

        labels = {
            
        }

        widgets = {
            'firstname' : forms.TextInput(attrs= {'class': 'inp', 'id': 'firstname', 'placeholder':'Enter Firstname'}),
            'middlename' : forms.TextInput(attrs= {'class': 'inp', 'id': 'middlename', 'placeholder':'Enter Middlename'}),
            'lastname' : forms.TextInput(attrs= {'class': 'inp', 'id': 'lastname', 'placeholder':'Enter Lastname'}),
            'rollno' : forms.TextInput(attrs= {'class': 'inp', 'id': 'rollno', 'placeholder':'Enter Roll Number'}),
            'course' : forms.Select(choices=course_choices),
            'gender' : forms.Select(choices=gender_choices),
            'phone' : forms.TextInput(attrs= {'class': 'inp', 'id': 'phone', 'placeholder':'Enter Phone Number'}),
            'address' : forms.Textarea(attrs= {'class': 'inp', 'id': 'address', 'placeholder':'Enter Address'}),
            'email' : forms.TextInput(attrs= {'class': 'inp', 'id': 'email', 'placeholder':'Enter Email Id'}),
            
        }