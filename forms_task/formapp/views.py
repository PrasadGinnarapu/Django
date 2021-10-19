from django.shortcuts import render
from . models import Student_Model
from . forms import Student

# # Create your views here.
# def base(request):

#     st_form = Student()

#     return render(request,'base.html', {"st_form": st_form})


def forms(request):
    if request.method == 'POST':
        st =Student(request.POST)
        if st.is_valid():
            nm = st.cleaned_data['Name']
            fnm = st.cleaned_data['Fname']
            ph = st.cleaned_data['Phno']
            em = st.cleaned_data['Email']


        data = Student_Model(Name=nm,Fname=fnm,Phno=ph,Email=em)
        data.save()
    
    else:
        st = Student()
        
    return render(request,'base.html',{'st':st})

