from django.shortcuts import render, HttpResponseRedirect
from .forms import UserRegister
from .models import User
# Create your views here.

#def addUser(request):
#    ur = UserRegister()
#    return render(request, 'UserSignUP.html', {'UserForm':ur})



def add_show(request):
 if request.method == 'POST':
  UR = UserRegister(request.POST)
  if UR.is_valid():
   uName = UR.cleaned_data['UserName']
   phn = UR.cleaned_data['PhoneNo']
   emai = UR.cleaned_data['Email']
   dob = UR.cleaned_data['DOB']
   gnd = UR.cleaned_data['Gender']
   ctry = UR.cleaned_data['Country']
   des = UR.cleaned_data['Description']
   #img = UR.cleaned_data['UploadImage']
   pwd = UR.cleaned_data['Password']
   atc = UR.cleaned_data['Agree_Terms']
   reg = User(UserName=uName, PhoneNo=phn, Email=emai, DOB=dob, Gender=gnd, Country=ctry,
              Description=des,  Password=pwd, Agree_Terms=atc)
  #UploadImage=img

   reg.save()
   UR = UserRegister()
 else:
  UR = UserRegister()
 USR = User.objects.all()
 return render(request, 'UserSignUP.html', {'form':UR, 'USR':USR})

def updateUser(request, id):
 if request.method == 'POST':
  pi = User.objects.get(pk=id)
  UR = UserRegister(request.POST, instance=pi)
  if UR.is_valid():
   UR.save()
 else:
  pi = User.objects.get(pk=id)
  UR = UserRegister(instance=pi)
 return render(request, 'updateuser.html', {'form':UR})

# This Function will Delete
def deleteUser(request, id):
 if request.method == 'POST':
  pi = User.objects.get(pk=id)
  pi.delete()
  return HttpResponseRedirect('/')
