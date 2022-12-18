from django.contrib.auth.decorators import login_required
from rest_framework import serializers, status, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Helpers import role_is_authorized
from Student.models import Student
from Student.serializers import StudentSerializer


@api_view(["POST"])
def add_student(request):
    student = StudentSerializer(data=request.data)

    if Student.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Student already exists')

    if student.is_valid():
        student.save()
        return Response(student.data)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@login_required()
def get_students(request):
    students = Student.objects.all()
    if students is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if role_is_authorized(request, "student"):
        return Response("you are not allowed to make this request", status=status.HTTP_403_FORBIDDEN)
    else:
        print(request.user.is_superuser)
        serialized_student = StudentSerializer(students, many=True)
        return Response(serialized_student.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if student is not None:
        serialized_student = StudentSerializer(student)
        return Response(serialized_student.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if student is not None:
        student.delete()
        return Response("student with id" + " " + str(student_id) + " deleted", status=status.HTTP_200_OK)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def update_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if student is not None:
        serialized_student = StudentSerializer(instance=student, data=request.data)
        if serialized_student.is_valid():
            serialized_student.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_404_NOT_FOUND)

