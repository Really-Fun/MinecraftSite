from django.urls import path
from minecraft import urls
import minecraft.views as views

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("about/", views.AboutPage.as_view(), name="about"),
    path("contacts/", views.ContactsPage.as_view(), name="contacts"),
    path("donate/", views.DonatePage.as_view(), name="donate"),
]