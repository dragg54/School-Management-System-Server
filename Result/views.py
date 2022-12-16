from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Helpers import validate_role
from Result.models import Result
from Result.serializers import ResultSerializer


@api_view(["POST"])
def add_result(request):
    user_role = "teacher"
    result = ResultSerializer(data=request.data)
    if Result.objects.filter(**request.data).exists():
        raise serializers.ValidationError("result already exists")
    if not validate_role(request, role):
        return Response("you are not authorized to make this request", status=status.HTTP_401_UNAUTHORIZED)
    if result.is_valid():
        result.save()
        return Response(result.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
