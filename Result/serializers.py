from rest_framework import serializers
from Result.models import Result


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['course_id', 'student_id', 'test_score_obtainable', 'test_score_obtained', 'exam_score_obtainable',
                  'exam_score_obtained']
