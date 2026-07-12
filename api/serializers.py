from rest_framework import serializers
from students.models import Student, Department,Course
from accounts.models import CustomUser
from rest_framework import generics
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "role",
        ]


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"
        
class courseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    department = DepartmentSerializer(read_only=True)
    courses = courseSerializer(many=True)

    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "dob",
            "gender",
            "cgpa",
            "photo",
            "department",
            "courses",

        ]

class StudentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "dob",
            "gender",
            "cgpa",
            "photo",
            "department",
            "courses",
        ]