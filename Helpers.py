from Role.models import Role


def role_is_authorized(request, role):
    current_user_id = request.user.id
    # generate current user role from current_user_id
    current_user_role = Role.objects.get(pk=current_user_id)
    return role == current_user_role.role_name
