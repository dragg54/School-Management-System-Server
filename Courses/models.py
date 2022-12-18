from django.db import models
from Student.models import Student

class Courses(models.Model):
    course_title = models.CharField(max_length=20)
    student = models.ForeignKey(Student, on_delete= models.CASCADE)

    def __str__(self):
        return self.course_title