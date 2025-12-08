# from django.shortcuts import render , HttpResponse 

 

# def home(request):                   
#     return HttpResponse("Hello from myapp this is my first project")
# def about(request):
#     return render(request, 'home.html')

# def project(request):
#     return HttpResponse("this is my project")
# def exprience(request):
#     return HttpResponse(" i have not exprience i am fresher")

from django.shortcuts import render, HttpResponse
from myapp.models import Contact
def home(request):
     return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def project(request):
   return render(request, 'project.html')

from django.shortcuts import render, redirect
from .models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        ins=Contact( name=name,
            email=email,
            phone=phone,
            message=message)
        ins.save()
        print("data submitted successfully")
       

        return redirect('contact')  # page refresh problem fix

    return render(request, 'contact.html')


def exprience(request):
    return HttpResponse("i have no experience, i am fresher")
