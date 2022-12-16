from django.urls import path, include
from . import views as student_view
from .views import LoginAPI
from knox import views as knox_views

urlpatterns = [
    path("addstudent", student_view.add_student, name="add student"),
    path("", student_view.get_students, name="get students"),
    path("/<str:student_id>", student_view.get_student, name="get student"),
    path("/<str:student_id>/delete", student_view.delete_student, name="delete student"),
    path("/<str:student_id>/update", student_view.update_student, name="update student"),
]
