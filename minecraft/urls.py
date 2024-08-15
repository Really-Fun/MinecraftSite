from django.urls import path
import minecraft.views as views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("", cache_page(30)(views.HomePage.as_view()), name="home"),
    path("about/", views.AboutPage.as_view(), name="about"),
    path("contacts/", views.ContactsPage.as_view(), name="contacts"),
    path("donate/", views.DonatePage.as_view(), name="donate"),
    path(
        "news/<int:server>/<slug:new>",
        cache_page(5 * 60)(views.NewPage.as_view()),
        name="new",
    ),
]
