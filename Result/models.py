from django.contrib.auth.models import User
from django.db import models
from Courses.models import Courses

class Result(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    student_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    test_score_obtainable = models.CharField(max_length=3)
    test_score_obtained = models.CharField(max_length=3)
    exam_score_obtainable = models.CharField(max_length=3)
    exam_score_obtained = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.course_id} result'
