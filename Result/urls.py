from django.urls import path
from . import views

urlpatterns = [
    path("", views.check_result, name="check result"),
    path("results/", views.get_results, name="get results"),
    path("<str:student_id>", views.get_result, name="get_result"),

]
