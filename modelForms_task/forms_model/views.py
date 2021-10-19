from django.shortcuts import render
from .forms import model_form1
from .models import model_forms_model


# Create your views here.
def model_forms(request):
    fm = model_form1() 
    return render(request,'regestration.html',context={'fm':fm})


def thank_page(request):
    fm = model_form1(request.POST)
    if request.method =='POST':
        if fm.is_valid():
            stid = fm.cleaned_data['Stid']
            fnm = fm.cleaned_data['Fname']
            mnm = fm.cleaned_data['Mname']
            lnm = fm.cleaned_data['Lname']
            phno = fm.cleaned_data['Phno']
            email = fm.cleaned_data['Email']
            cmpny = fm.cleaned_data['Company']
            crse = fm.cleaned_data['Course']
            data = model_forms_model(Fname=fnm,Mname=mnm,Lname=lnm,Phno=phno,Email=email,Company=cmpny,Course=crse,Stid=stid)
            data.save()

    return render(request,'thanks.html')