from rest_framework import serializers
from students.models import Student, Department,Course
from accounts.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = {
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "role",            
        }

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = " __all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class Studentserializer(serializers.ModelSerializer):
    
    user=UserSerializer(read_only=True)
    department=DepartmentSerializer(read_only=True)
    courses=CourseSerializer(many=True,read_only=True)

    class meta:
        model = Student
        fields = {
            "id",
            "user",
            "dob",
            "gender",
            "cgpa",
            "department",
            "courses",
            "photo",
        }