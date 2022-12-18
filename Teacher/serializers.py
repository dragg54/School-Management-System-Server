from rest_framework import serializers

from Student.models import Student
from Teacher.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name','role', 'sex', 'email', 'subject', 'salary', 'next_of_kin', 'date_employed')