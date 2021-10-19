from django import forms
from django.forms import fields
from .models import model_forms_model

class model_form1(forms.ModelForm):
    # name=forms.CharField(max_length=30)
    # email = forms.EmailField(required=False)
    
    class Meta():
        model = model_forms_model
        # fields = '__all__'

        fields = ['Stid','Fname','Mname',"Lname",'Phno','Email','Company','Course']
        # labels = {"stid":'Enter your student id :',
        # "Fname" :'Enter your name :',
        # 'Phno':'Enter your ph number',
        # 'Email':'Enter your email id :',
        # 'Company':'Enter your comapany name :',
        # 'Course' : 'Enter your course name :',
        # }