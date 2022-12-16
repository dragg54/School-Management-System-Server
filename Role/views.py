from django.shortcuts import render

from Role.models import Role


def get_current_user_role(request):
    current_user = request.user
    current_user_id = current_user.id
    current_user_role = Role.objects.get(pk=current_user_id)
    return current_user_role
