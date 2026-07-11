from rest_framework.views import APIView
from rest_framework.response import Response

class ApiHome(APIView):
    def get(self,request):
        return Response({"message":"Student Management System",
                         "version":"1.0.0",
                         "status":"running"
                         })
