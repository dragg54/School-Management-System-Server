from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from django.shortcuts import render
from rest_framework import serializers, status, generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Student.models import Student
from Student.serializers import StudentSerializer, UserSerializer, RegisterSerializer


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
    else:
        print(request.user)
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


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
