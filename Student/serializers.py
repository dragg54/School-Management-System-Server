from django.contrib.auth.models import User
from rest_framework import serializers

from Student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'first_name', 'last_name', 'sex', 'email', 'age', 'student_class', 'next_of_kin',
                  'session_fee_payable', 'session_fee_paid', 'role', 'date_admitted']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'], last_name=validated_data['last_name'],
                                        first_name=validated_data['first_name'])
        return user
