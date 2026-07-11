from django import template
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import Templateview
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name="registration/login.html"
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy("home")
    
    class ProfileView(LoginRequiredMixin,Templateview):
        template_name="registration/profile.html"