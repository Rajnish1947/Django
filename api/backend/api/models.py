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