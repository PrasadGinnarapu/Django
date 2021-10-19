from django import forms
from django.db.models.fields import DateField
from django.forms.widgets import DateInput, RadioSelect, Select, SelectDateWidget, Textarea
from .models import Student_model

class Student_form(forms.ModelForm):
    class Meta():
        model = Student_model
        fields = '__all__'
        gender_choice = [('M','Male'),('F','Female')]
        level_choices = [('1st year','FIRST YEAR'),('2nd year','SECOND YEAR'),('3rd year','THIRD YEAR'),('4th year','FOURTH YEAR')]
        widgets = {'Gender' : forms.RadioSelect(choices=gender_choice),
                    'Yourlevel': Select(choices = level_choices),
                    'Address' : forms.Textarea(attrs={'class':'form-control'}),
                    'Fname' : forms.TextInput(attrs={'class':'form-control'}),
                    'Lname' : forms.TextInput(attrs={'class':'form-control'}),
                    'FatherName' : forms.TextInput(attrs={'class':'form-control'}),
                    'TelNo' : forms.NumberInput(attrs={'class':'form-control'}),
                    'HighSchoolName' : forms.TextInput(attrs={'class':'form-control'}),
                    'Address' : forms.TextInput(attrs={'class':'form-control'}),
                    'Email' : forms.EmailInput(attrs={'class':'form-control'}),
                }