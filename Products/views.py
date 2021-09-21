from django.shortcuts import render
from . import views

# Create your views here.

def home(request):
    return render(request, 'home.html')

def gallery(request):
    return render(request, 'gallery.html')

def new_collection(request):
    return render(request, 'newcollection.html')

def ancient_collection(request):
    return render(request, 'ancientcollection.html')

def about(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contactus.html')