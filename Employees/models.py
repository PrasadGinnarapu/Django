from django.db import models

# Create your models here.

class Emp(models.Model):
    empId = models.IntegerField()
    empName = models.CharField(max_length=70)
    empEmail = models.EmailField(max_length=70)
    empMobile = models.IntegerField(max_length=15)


