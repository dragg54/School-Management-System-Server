"""School_Management_System_Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from knox import views as knox_views
import Courses
import Student.views
from Student.views import LoginAPI, RegisterAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/student/', include("Student.urls"), name="student"),
    #path('api/teacher/', include("Teacher.urls"), name="teacher"),
    path('login', LoginAPI.as_view(), name='login'),
    path('logout', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('register', RegisterAPI.as_view(), name='register'),
    path('api/auth/', include('knox.urls')),
    path("api/result/", include("Result.urls"), name="result"),
    path("user", Student.views.get_current_user, name="current user"),
    path("api/course/", include("Courses.urls"), name="course")
]
