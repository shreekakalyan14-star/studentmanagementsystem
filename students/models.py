from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    building = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):  # Renamed to PascalCase
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    credits = models.IntegerField()

    def __str__(self):
        return self.name

class Student(models.Model):  # Renamed to PascalCase
    GENDER_CHOICES = [  # Fixed: assignment and proper list
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    dob = models.DateField()  # Fixed: DateField not DataField
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    photo = models.ImageField(upload_to='student_photos/', null=True)
    department = models.ForeignKey(
        Department, 
        on_delete=models.CASCADE, 
        related_name='students'
    )  # Fixed: added missing comma and line break for readability
    courses = models.ManyToManyField(Course, blank=True)  # Uses corrected class name
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Fixed: updated_at not updates_at

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # Fixed: uses existing fields