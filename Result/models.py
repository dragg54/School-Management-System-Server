from django.db import models
from Courses.models import Courses
from Student.models import Student


class Result(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test_score_obtainable = models.CharField(max_length=3)
    test_score_obtained = models.CharField(max_length=3)
    exam_score_obtainable = models.CharField(max_length=3)
    exam_score_obtained = models.CharField(max_length=3)

    def __str__(self):
        return self.course + "result"
