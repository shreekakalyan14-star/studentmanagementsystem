from django import template
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")
    
# FIX 1: Add CustomLogoutView so urls.py can find it
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")

# FIX 2: Moved back to the left margin (no longer indented inside the login view)
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "registration/profile.html"
