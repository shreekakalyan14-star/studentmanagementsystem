from django.contrib import admin

# Register your models here.

from .models import Student,Course,Department

@admin.register(Department)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'building')
    search_fields = ('name',)

    @admin.register(Course)

    class CourseAdmin(admin.ModelAdmin):
        list_display = ('id',
                        'name',
                        'code',
                        'credits')
        search_fields=('name','code')
        
    @admin.register(Student)

    class StudentAdmin(admin.ModelAdmin):
        list_display=('id',
                      'first_name',
                      'last_name',
                      'email',
                      'department',
                      'cgpa',
        )
        list_filter=('department','gender')
        search_fields=('first_name','last_name','email')
        filter_horizontal=('courses',)