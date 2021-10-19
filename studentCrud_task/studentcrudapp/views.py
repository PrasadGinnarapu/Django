from django.shortcuts import render
from .models import Student_model
from .forms import Student_form

# Create your views here.
def register(request):
    sf = Student_form()
    return render(request,'reg.html',{'sf':sf})
def datasave(request):
    if request.method == 'POST':
        sf = Student_form(request.POST)
        if sf.is_valid():
            fnm = sf.cleaned_data['Fname']
            lnm = sf.cleaned_data['Lname']
            father_name = sf.cleaned_data['FatherName']
            gn = sf.cleaned_data['Gender']
            tel = sf.cleaned_data['TelNo']
            hsn = sf.cleaned_data['HighSchoolName']
            add = sf.cleaned_data['Address']
            level = sf.cleaned_data['Yourlevel']
            email = sf.cleaned_data['Email']
            data = Student_model(Fname=fnm,Lname=lnm,FatherName=father_name,Gender=gn,TelNo=tel,
                        HighSchoolName=hsn,Address=add,Yourlevel=level,Email=email)
            data.save()
    return render(request,'reg.html')
