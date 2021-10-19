from django.db import models

# Create your models here.
class Student_model(models.Model):
    name = models.CharField(max_length=30)
    Phno = models.IntegerField()
    email=  models.EmailField(max_length=30)
    def clean_