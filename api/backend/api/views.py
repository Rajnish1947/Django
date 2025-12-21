from django.shortcuts import render
from django.http import HttpResponse
from api.models import companyDetails ,Employee
from api.serializers import companySerilizer ,EmployeeSerializer
from rest_framework import viewsets
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=companyDetails.objects.all()
    serializer_class=companySerilizer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer