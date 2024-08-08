from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class LoginForm(AuthenticationForm):
    

    class Meta:
        model = get_user_model()
        fields = ["username", "password"]


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=50,
        label="Придумайте логин",
        widget=forms.TextInput(attrs={"class": "form-input"}),
    )
    password1 = forms.CharField(
        max_length=50,
        label="Придумайте пароль",
        widget=forms.PasswordInput(
            {
                "class": "password-input",
            }
        ),
    )
    password2 = forms.CharField(
        max_length=50,
        label="Повторите пароль",
        widget=forms.PasswordInput(
            {
                "class": "password-input",
            }
        ),
    )

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password1", "password2"]
        labels = {
            "email": "Введите имейл",
        }
        widgets = {
            "email": forms.EmailInput(attrs={"class": "email-field"}),
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой e-mail уже существует")
        return email
