from django.core import validators
from django import forms
from .models import User

class UserRegister(forms.ModelForm):
 class Meta:
  model = User
  fields = '__all__'
  #fields = ['UserName', 'Email', 'Gender', 'DOB','Country','Description','UploadImage','Password','Agree_Terms']
  gender = [('M', 'Male'), ('F', 'Female')]

  countries = [('IND', 'INDIA'),
               ('US', 'USA'),
               ('CHN', 'CHINA')]
  widgets = {
    'UserName': forms.TextInput(attrs={'class':'form-control'}),
    'PhoneNo': forms.NumberInput(attrs={'class':'form-control'}),
    'Email': forms.EmailInput(attrs={'class':'form-control'}),
    'Gender': forms.RadioSelect(attrs={'class':'form-check-input '}, choices=gender),
    'DOB': forms.DateTimeInput(attrs={'class':'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'}),
    'Country': forms.Select(attrs={'class':'form-control'}, choices=countries),
    'Description': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
    #'UploadImage': forms.FileInput(attrs={'class':'form-control'}),
    'Password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
    'Agree_Terms': forms.CheckboxInput(attrs={'class':'form-check-input'}),
  }

