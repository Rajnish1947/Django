# serializer does
# Converts model → JSON (for API response)
# Converts JSON → model (for POST/PUT requests)
from django.db import models

# Create your models here.
class companyDetails(models.Model):
    useId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    about=models.TextField()
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

class Employee(models.Model):
   
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(unique=True)
    joining_date = models.DateField()    
    company = models.ForeignKey(
        companyDetails,
        on_delete=models.CASCADE,   # ✅ delete company → employees auto delete
        
    )