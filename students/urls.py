from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.student_list, name='student_list'),
    path('<int:student_id>/', views.student_details, name='student_details'),
]
