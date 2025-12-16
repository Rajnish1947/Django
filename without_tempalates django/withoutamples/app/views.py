from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def firstview(request):
    return HttpResponse (" this is ur http request")

def second(request):
    return HttpResponse("this is our second request")

def makeany(request):
    return HttpResponse("we can make any request")