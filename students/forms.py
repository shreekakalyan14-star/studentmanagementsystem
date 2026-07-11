from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student

        fields=[
            'dob',
            'gender',
            'cgpa',
            'photo',
            'department',
            'courses',
        ]
        widgets={
            'dob':forms.DateInput(attrs={'type':'data'}),
            'courses':forms.CheckboxSelectMultiple()
        }


        def clean_email(self):
            email=self.cleaned_data['email']
            if Student.objects.filter(email=email).excludes(pk=self.instance.pk).exists():
                raise forms.ValidationError("Thid email is already in use.")
            return email
        
        def clean_cgpa(self):
            cgpa=self.cleaned_data['cgpa']
            if cgpa <0 or cgpa >10:
                raise forms.ValidationError("CGPA musdt be between 0 and 10,")
            return cgpa