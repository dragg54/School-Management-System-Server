from django.urls import path
from Courses import views

urlpatterns = [
    path("<str:student_id>", views.get_course, name="courses")
]