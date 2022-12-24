from django.db import models
from Student.models import Student


class Courses(models.Model):
    session = models.CharField(default="2020/2021", max_length=9, null=True)
    course_title = models.CharField(max_length=20)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_title
