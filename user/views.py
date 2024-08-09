from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from user.forms import RegisterForm, LoginForm, EditProfileForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "user/register.html"
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy("profile")


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = "user/profile.html"
    extra_context = {"title": "Профиль"}
    context_object_name = "profile"

    def get_object(self, queryset=None):
        return self.request.user


class LoginProfileView(LoginView):
    template_name = "user/login.html"
    form_class = LoginForm
    extra_context = {"title": "Авторизация пользователя"}

    def get_success_url(self) -> str:
        return reverse("profile")


def logout_profile(request: HttpRequest) -> HttpResponse:
    logout(request=request)
    return redirect("home")


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = EditProfileForm
    template_name = "user/edit_profile.html"
    extra_context = {"title": "EditProfile"}

    def get_success_url(self) -> str:
        return reverse_lazy("profile")

    def get_object(self):
        return self.request.user

    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)
