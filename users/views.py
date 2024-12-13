from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView


class UserLoginView(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("home")  # Change 'home' to your home page URL name


class UserRegisterView(CreateView):
    template_name = "users/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("users:login")
