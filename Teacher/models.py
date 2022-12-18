from django.contrib.auth.models import User
from django.db import models


class Teacher(models.Model):
    objects = None
    teacher_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    role = models.CharField(max_length=20, default="teacher")
    sex = models.CharField(max_length=1)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    salary = models.CharField(max_length=10)
    next_of_kin = models.CharField(max_length=20)
    date_employed = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.first_name
