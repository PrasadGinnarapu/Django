from django.contrib import admin
from .models import Student_model

# Register your models here.
@admin.register(Student_model)
class Student_database(admin.ModelAdmin):
    list_display = ['Fname','Lname','FatherName','Gender','TelNo','HighSchoolName','Address','Yourlevel','Email']