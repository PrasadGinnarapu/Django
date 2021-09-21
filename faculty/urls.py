from django.urls import path
from . import views

urlpatterns = [

    path('teach/', views.teachers),
]
