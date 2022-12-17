from django.urls import path
from . import views

urlpatterns=[
    path("/results", views.get_results, name="get results"),
    path("", views.check_result, name="check result")
]