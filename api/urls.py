from django.urls import path,include
from .views import ApiHome

urlpatterns=[
    path('',ApiHome.as_view()),
]