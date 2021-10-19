from django.db import models

# Create your models here.
class model_forms_model(models.Model):
    Stid = models.IntegerField()
    Fname = models.CharField(max_length=30)
    Mname = models.CharField(max_length=30)
    Lname = models.CharField(max_length=30)
    Phno = models.IntegerField()
    Email = models.EmailField(max_length=50)
    Company = models.CharField(max_length=30)
    Course = models.CharField(max_length=30)

    def __str__(self):
        return self.Fname