from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from user.forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


# Create your views here.
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "user/register.html"
    extra_context = {"title": "Регистрация"}
    # success_url = reverse_lazy("home")


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = "user/profile.html"
    extra_context = {"title": "Профиль"}
    context_object_name = "profile"

    def get_object(self, queryset=None):
        return self.request.user


class LoginView(LoginView):
    template_name = "user/login.html"
    form_class = LoginForm
    extra_context = {"title": "Авторизация пользователя"}

    def get_success_url(self) -> str:
        return reverse("profile")
