from django.shortcuts import render
from . import views
from . models import Emp

# Create your views here.

def home(request):
    return render(request, 'home.html')

def employees(request):
    emp = Emp.objects.all()
    return render(request, 'employees.html', {'empdetails':emp})
