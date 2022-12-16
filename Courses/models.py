from django.db import models

from Student.models import Student
#from Teacher.models import Teacher


class Courses(models.Model):
    course_title = models.CharField(max_length=20)
    #teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete= models.CASCADE)

    def __str__(self):
        return self.course_title