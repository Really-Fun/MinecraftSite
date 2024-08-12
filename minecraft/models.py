from django.db import models
from django.urls import reverse


# Create your models here.
class Servers(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя сервера", blank=True)
    slug = models.SlugField(
        max_length=25, verbose_name="Слаг", unique=True, blank=False
    )
    max_online = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сервер"
        verbose_name_plural = "Серверы"


class News(models.Model):
    title = models.CharField(
        max_length=40,
        unique=True,
        blank=False,
        verbose_name="Название новости",
        name="title",
    )
    text = models.TextField(
        max_length=10000,
        unique=False,
        blank=False,
        verbose_name="Содержание новости",
    )
    image = models.ImageField(
        upload_to="media/news/%Y/%m/%d/",
        default="media/MinecraftLogo.png",
        verbose_name="Изображение новости",
    )
    time_create = models.DateTimeField(verbose_name="Дата создания", auto_now=True)
    time_update = models.DateTimeField(
        verbose_name="Дата обновления", auto_now_add=True
    )
    slug = models.SlugField(
        verbose_name="Слаг",
        max_length=50,
    )
    is_published = models.BooleanField(verbose_name="Опубликована", default=False)
    server = models.ForeignKey(
        "Servers",
        related_name="serv",
        on_delete=models.DO_NOTHING,
        verbose_name="Наименование сервера",
    )

    def get_absolute_url(self):
        return reverse("new", kwargs={"server": self.server_id, "new": self.slug})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
