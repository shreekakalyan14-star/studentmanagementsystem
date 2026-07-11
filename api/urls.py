from django.urls import path,include
from .views import ApiHome,StudentListAPI

urlpatterns=[
    path('',ApiHome.as_view()),

    path('students/',StudentListAPI.as_view(),name='student_api'),
]