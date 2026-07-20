from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from students.models import Student

from .serializers import (
    StudentSerializer,
    StudentWriteSerializer,
)


from rest_framework.permissions import IsAuthenticated


class StudentListCreateAPI(generics.ListCreateAPIView):

    permission_classes=[IsAuthenticated]

    queryset = Student.objects.select_related(
        "user",
        "department",
    ).prefetch_related("courses")

    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields=["gender","department",]

    search_fields=["user__first_name",
                   "user__last_name",
                   "user__email",
                   "department__name"]
    
    ordering_fields=["cgpa",
                     "dob",
                     "user__first_name"]
    
    ordering=["user__first_name"]

    def get_serializer_class(self):

        if self.request.method == "POST":
            return StudentWriteSerializer

        return StudentSerializer


class StudentRetrieveUpdateDestroyAPI(
    generics.RetrieveUpdateDestroyAPIView
):
    
    permission_classes=[IsAuthenticated]

    queryset = Student.objects.select_related(
        "user",
        "department"
    ).prefetch_related("courses")

    def get_serializer_class(self):

        if self.request.method in ["PUT", "PATCH"]:
            return StudentWriteSerializer

        return StudentSerializer
    
