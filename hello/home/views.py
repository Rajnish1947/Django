from django.shortcuts import HttpResponse , render 

# Create your views here.
def index(request):
    context = {
        "title": "rajnish Page",
        "message": "Welcome  to the Index Page! this is my first django project",
    }
    return render(request, "index.html", context)
def about(request):
    return HttpResponse("Hello, world. You're at the about index.")

def services(request):
    return HttpResponse("Hello, world. You're at the services index.")
def contact(request):
    return HttpResponse("Hello, world. You're at the contact index.")
