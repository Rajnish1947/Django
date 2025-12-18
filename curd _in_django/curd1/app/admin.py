from django.contrib import admin

# Register your models here.
# admin form yaha khud se change karenge like form me kya 
# form me kya kya dekhana hai 
from .models import  Student

@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','username','message']
