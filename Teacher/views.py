from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Teacher.models import Teacher
from Teacher.serializers import TeacherSerializer


# Create your views here.
@api_view(["POST"])
def add_student(request):
    student = TeacherSerializer(data=request.data)

    if Teacher.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Student already exists')

    if student.is_valid():
        student.save()
        return Response(student.data)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
