from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm

def register(request):
    if request.method== 'POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Account create successfully')
            return redirect('login')
        
        else:
            form=RegisterForm()
        return render(request,'registration/register.html',{'form':form})

# Create your views here.
