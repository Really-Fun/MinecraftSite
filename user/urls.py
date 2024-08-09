from django.urls import path
from user.views import (
    RegisterView,
    ProfileView,
    LoginProfileView,
    EditProfileView,
    logout_profile,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("login/", LoginProfileView.as_view(), name="login"),
    path("login/", logout_profile, name="logout"),
    path("profile/edit/", EditProfileView.as_view(), name="edit"),
]
