from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def info(request):

    return HttpResponse("Hello this is Students application ")