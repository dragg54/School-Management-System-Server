from rest_framework import serializers

from Courses.models import Courses


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"
