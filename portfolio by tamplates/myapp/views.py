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

def home(request):
     return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def project(request):
   return render(request, 'project.html')

def contact(request):
    if request.method == "POST":   # ✅ CORRECT
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        print(name,email,phone,message)

    return render(request, 'contact.html')

def exprience(request):
    return HttpResponse("i have no experience, i am fresher")
