from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, TemplateView, DetailView
from minecraft.models import News
from minecraft.service import get_online_servers


# Create your views here.
class HomePage(ListView):
    template_name = "minecraft/index.html"
    extra_context = {
        "title": "AdventTime",
        "servers": get_online_servers([("209.222.115.129", "25565")]),
    }
    allow_empty = True
    model = News
    context_object_name = "news"

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class AboutPage(TemplateView):
    template_name = "minecraft/about.html"
    extra_context = {"title": "О нас"}


class ContactsPage(TemplateView):
    template_name = "minecraft/contacts.html"
    extra_context = {"title": "Контакты"}


class DonatePage(TemplateView):
    template_name = "minecraft/donate.html"
    extra_context = {"title": "Донат"}


class NewPage(DetailView):
    template_name = "minecraft/new.html"
    model = News
    context_object_name = "new"
    extra_context = {"title": "Новсть"}

    def get_object(self, queryset=None):
        server_id = self.kwargs.get("server")
        new_slug = self.kwargs.get("new")
        return News.objects.get(server_id=server_id, slug=new_slug)
