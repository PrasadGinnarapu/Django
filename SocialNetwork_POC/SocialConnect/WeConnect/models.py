from django.db import models

# Create your models here.
class User(models.Model):
     UserName = models.CharField(max_length=10)
     PhoneNo = models.IntegerField()
     Email = models.EmailField(max_length=15)
     DOB = models.DateField()
     Gender = models.CharField(max_length=10)
     Country = models.CharField(max_length=10)
     Description = models.CharField(max_length=100)
     #UploadImage = models.ImageField(upload_to="images/")
     Password = models.CharField(max_length=10)
     Agree_Terms = models.BooleanField(default=False)



