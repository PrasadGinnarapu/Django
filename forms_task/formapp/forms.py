from django import forms
from django.forms.fields import IntegerField

class Student(forms.Form):
    Name = forms.CharField(max_length=26, required=True)
    Fname = forms.CharField( max_length=30, required=False)
    Phno = forms.IntegerField()
    Email = forms.EmailField(required=True)
    