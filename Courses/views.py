from django.shortcuts import render
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Courses.models import Courses
from Courses.serializers import CourseSerializer


@api_view(["POST"])
def add_course(request):
    course = CourseSerializer(data=request.data)
    if course.is_valid():
        course.save()
        return Response(course.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_course(request, student_id):
    courses = Courses.objects.filter(student=student_id)
    if courses is not None:
        serialized_courses = CourseSerializer(courses, many=True)
        return Response(serialized_courses.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

