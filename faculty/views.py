from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def teachers(request):

    a = "Hello Srinitha"
    return HttpResponse(a)

