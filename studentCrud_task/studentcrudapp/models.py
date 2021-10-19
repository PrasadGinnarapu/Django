from django.db import models

# Create your models here.
class Student_model(models.Model):
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    FatherName = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    # DOB = models.IntegerField()
    TelNo = models.IntegerField()
    HighSchoolName = models.CharField(max_length=60)
    Address = models.CharField(max_length=100)
    Yourlevel = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)

    def __str__(self) :
        return self.Fname
