from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Courses.serializers import CourseSerializer


@api_view(["POST"])
def add_course(request):
    course = CourseSerializer(data=request.data)
    if course.is_valid():
        course.save()
        return Response(course.data, status=status.HTTP_200_OK)
