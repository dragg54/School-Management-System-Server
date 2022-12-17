from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Helpers import role_is_authorized
from Result.models import Result
from Result.serializers import ResultSerializer


@api_view(["POST"])
def add_result(request):
    user_role = "teacher"
    result = ResultSerializer(data=request.data)
    if Result.objects.filter(**request.data).exists():
        raise serializers.ValidationError("result already exists")
    if not role_is_authorized(request, user_role):
        return Response("you are not authorized to make this request", status=status.HTTP_401_UNAUTHORIZED)
    if result.is_valid():
        result.save()
        return Response(result.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_results(request):
    user_role = "teacher"
    if not role_is_authorized(request, user_role):
        return Response("you are not authorized to make this request", status=status.HTTP_401_UNAUTHORIZED)
    results = Result.objects.all()
    if results is not None:
        serialized_result = ResultSerializer(results, many=True)
        return Response(serialized_result.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def check_result(request):
    user_role = "student"
    if not role_is_authorized(request, user_role):
        return Response("you are not authorized to make this request", status=status.HTTP_401_UNAUTHORIZED)
    result = Result.objects.filter(student_id=request.user.id)
    if result is not None:
        serialized_result = ResultSerializer(result, many=True)
        return Response(serialized_result.data, status=status.HTTP_200_OK)
