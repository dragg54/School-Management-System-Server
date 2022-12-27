from django.contrib.auth.models import User
from django.db import models
from Courses.models import Courses
from Student.models import Student


class Result(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    test_score_obtainable = models.CharField(max_length=3)
    test_score_obtained = models.CharField(max_length=3)
    exam_score_obtainable = models.CharField(max_length=3)
    exam_score_obtained = models.CharField(max_length=3)
    grade = models.CharField(max_length=1, null=True)

    def __str__(self):
        student = Student.objects.get(id = self.student_id.id)
        return f'{student.first_name} {student.last_name} {self.course_id} result'
