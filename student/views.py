from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Students
from .models import Groups
from .models import Status

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

def info_group(request, groups_id):
     prods = Students.objects.filter(number_group=groups_id)
     return render(request,"templates_student/about_group.html",{"info_group": prods} )

def create(request):
     groups = Groups.objects.all()
     statuses = Status.objects.all()
     return render(request, 'templates_student/create_student.html',
                   {"groups": groups, "statuses": statuses})
     
def save(request):
     print(request.POST)
     if request.POST['status'] is not None:
          save_student=Students.objects.create(secondname=request.POST['secondname'],
                                          name=request.POST['name'],
                                          thirdname=request.POST['thirdname'],
                                          birthday=request.POST['birthday'],
                                          number_group_id=request.POST['number_group'],
                                          status_id=request.POST['status'])
     save_student.save()
     return HttpResponseRedirect(reverse("student:index"))

