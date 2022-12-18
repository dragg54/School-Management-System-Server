from django.contrib.auth.models import User
from rest_framework import serializers

from Student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'sex', 'email', 'age', 'student_class', 'next_of_kin',
                  'session_fee_payable', 'session_fee_paid', 'role', 'date_admitted']


