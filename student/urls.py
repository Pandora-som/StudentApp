from django.urls import path

from . import views

app_name = 'student'
urlpatterns = [
    path("", views.index, name="index"),
    path("students/", views.students, name="students"),
    path("help/", views.help, name="groups"),
    path("student_info/<int:students_id>", views.student_info, name="students_info"),
    path("info_group/<int:groups_id>", views.info_group, name="infos_group"),
    path("create/", views.create, name="create"),
    path("save/", views.save, name="save"),
]
