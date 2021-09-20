from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employees', views.employees, name = 'empdetails'),

]
