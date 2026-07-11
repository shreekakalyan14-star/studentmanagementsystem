from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Studentserializer 
from students.models import Student
class ApiHome(APIView):
    def get(self,request):
        return Response({"message":"Student Management System",
                         "version":"1.0.0",
                         "status":"running"
                         })

class StudentListAPI(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=Studentserializer(students,many=True)
        return Response(serializer.data)