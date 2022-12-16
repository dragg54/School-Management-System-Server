from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_class = models.CharField(max_length=5)
    sex = models.CharField(max_length=1)
    email = models.EmailField()
    age = models.CharField(max_length=2)
    session_fee_payable = models.CharField(max_length=10)
    session_fee_paid = models.CharField(max_length=10)
    role = models.CharField(max_length=10)
    next_of_kin = models.CharField(max_length=30)
    date_admitted = models.DateField(auto_now=False)

    def __str__(self):
        return self.first_name + " " + self.last_name
