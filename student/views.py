from django.http import HttpResponse
from django.shortcuts import render
from .models import Students

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def students(request):
     prods = Students.objects.all()
     return render(request,"templates_student/students.html", {"students": prods})

