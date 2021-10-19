from django.db import models

# Create your models here.
class Student_Model(models.Model):
    Name = models.CharField(max_length=26)
    Fname = models.CharField( max_length=30)
    Phno = models.IntegerField()
    Email = models.EmailField()

    def __str__(self):
        return self.Name