from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_show, name='adduserform'),
    path('delete/<int:id>/', views.deleteUser, name="deletedata"),
    path('<int:id>/', views.updateUser, name="updatedata"),

    #path('', views.addUser, name='add')

]