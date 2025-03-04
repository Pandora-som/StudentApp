from django.http import HttpResponse
from django.shortcuts import render
from .models import Students
from .models import Groups

def index(request):
    return render(request, "templates_student/index.html")

def students(request):
     prods = Students.objects.all()
     return render(request,"templates_student/students.html", {"students": prods})

def help(request):
     prods = Groups.objects.all()
     return render(request,"templates_student/student_groups.html",{"help": prods} )

