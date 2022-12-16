from django.contrib.auth.models import User
from django.db import models

from Student.models import Student


class Role(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=50)