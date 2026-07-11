from django.shortcuts import get_object_or_404, render, redirect

import students  # ✅ Import redirect function
from .models import Course, Department, Student
from students.forms import StudentForm
from django.db.models import Avg
from django.contrib import messages

def home(request):
    total_students=Student.objects.count()
    total_departments=Department.objects.count()
    total_courses=Course.objects.count()
    avg_cgpa = Student.objects.aggregate(cgpa_avg=Avg('cgpa'))["cgpa_avg"]

    context={
        'total_students':total_students,
        'total_departments':total_departments,
        'total_courses':total_courses,
        'average_cgpa':avg_cgpa,
    }
    return render(request, 'home.html',context)


def student_list(request):
    search=request.GET.get('search')
    students=Student.objects.all()
    if search:
        students= students.filter(first_name__icontains=search)
    students= students.order_by('first_name')
    context = {
        'students': students,
        'search': search,
    }
    return render(request, 'students/student_list.html', context)


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    context = {
        'student': student
    }
    return render(request, 'students/student_detail.html', context)


def student_create(request):  # ✅ Removed redirect parameter
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Student added successfully')
            return redirect('student_list')  # ✅ redirect is now the imported function
    else:
        form = StudentForm()  # ✅ Indentation fixed - else aligned with `if request.method`
    
    return render(request, 'students/student_form.html', {'form': form, 'title': 'Create Student'})


def student_update(request, student_id):  # ✅ Removed redirect parameter
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,'Student updated successfully')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'students/student_form.html', {'form': form, 'title': 'Update Student'})


def student_delete(request, student_id):  # ✅ Removed redirect parameter
    student = get_object_or_404(Student, id=student_id)  # ✅ Fixed Student capitalization
    if request.method == 'POST':
        student.delete()
        messages.success(request,'Student deleted successfully')
        return redirect('student_list')
    return render(request, 'students/student_delete.html', {'student': student})  # ✅ Fixed dict key