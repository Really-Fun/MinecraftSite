from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, TemplateView
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
