from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Students
from .models import Groups

def index(request):
    return render(request, "templates_student/index.html")

def students(request):
     prods = Students.objects.all()
     return render(request, "templates_student/students.html", {"students": prods})

def help(request):
     prods = Groups.objects.all()
     return render(request,"templates_student/student_groups.html",{"help": prods} )

def student_info(request, students_id):
     prods = get_object_or_404(Students, pk=students_id)
     return render(request,"templates_student/student_info.html", {"student_info": prods})

# def info_group(request, groups_id):
#      prods = get_object_or_404(Students, pk=groups_id)
#      return render(request,"templates_student/about_group.html",{"info_group": prods} )
def info_group(request, groups_id):
     prods = Students.objects.filter(number_group=groups_id)
     return render(request,"templates_student/about_group.html",{"info_group": prods} )