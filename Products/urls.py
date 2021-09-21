from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('newcollection', views.new_collection, name='newcollection'),
    path('ancientcollection', views.ancient_collection, name='ancientcollection'),
    path('aboutus', views.about, name='aboutus'),
    path('contactus', views.contact, name='contactus'),
]