# from django.shortcuts import render

# ye sab function base view hai 
# from django.http import HttpResponse # Create your views here.

# def home(request):
#     return HttpResponse("api is working now")

# def displaycontact(request):
#     return render(request,'index.html')

# ab ham class base view banayenge

from django.views import View
from django.shortcuts import render, redirect ,get_object_or_404
from .models import Student
from .forms import AddStudentForm


class Home(View):

    def get(self, request):
        stu_data = Student.objects.all()
        form = AddStudentForm()
        return render(request, 'index.html', {
            'students': stu_data,
            'form': form
        })

    def post(self, request):
        form = AddStudentForm(request.POST)
        stu_data = Student.objects.all()

        if form.is_valid():
            form.save()
            return redirect('home')
 # refresh page after save

        return render(request, 'index.html', {
            'students': stu_data,
            'form': form
        })
class UpdateContact(View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = AddStudentForm(instance=student)
        students = Student.objects.all()

        return render(request, 'index.html', {
            'form': form,
            'students': students
        })

    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = AddStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return redirect('home')
class DeleteContact(View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()
        return redirect('home')
