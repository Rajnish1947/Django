from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# pip install django-cors-headers
# pip install djangorestframework
def Home(request):
    return HttpResponse("this is our view page app connected with project")

