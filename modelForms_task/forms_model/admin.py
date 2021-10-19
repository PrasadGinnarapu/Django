from django.contrib import admin
from .models import  model_forms_model

# Register your models here.
@admin.register(model_forms_model)
class Model_forms_admin(admin.ModelAdmin):
    list_display =['Fname','Lname','Phno','Email']
