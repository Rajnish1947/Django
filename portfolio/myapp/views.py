from django.shortcuts import render , HttpResponse 

 

def home(request):                   
    return HttpResponse("Hello from myapp this is my first project")
def about(request):                   
    return HttpResponse("Hello from myapp this is my first project")
def project(request):
    return HttpResponse("this is my project")
def exprience(request):
    return HttpResponse(" i have not exprience i am fresher")

