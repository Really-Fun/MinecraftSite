from django.urls import path
from user.views import RegisterView, ProfileView, LoginView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("login/", LoginView.as_view(), name="login")
]
