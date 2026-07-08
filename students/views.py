from django.shortcuts import render, get_object_or_404 # Changed to get_object_or_404
from .models import Student

def home(request):
    return render(request, 'home.html')

def student_list(request):
    # Capital 'S' used to reference the imported model
    students = Student.objects.all().order_by('first_name')

    context = {
        'students': students
    }

    return render(request, 'students/student_list.html', context)

def student_details(request, student_id):
    # Capital 'S' and get_object_or_404 used for a single item
    student = get_object_or_404(Student, id=student_id)

    context = {
        'student': student
    }

    return render(request, 'students/student_detail.html', context)
