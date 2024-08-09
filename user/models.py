from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.
class Donate(models.Model):
    name = models.CharField(
        verbose_name="Наименование доната",
        max_length=50,
        blank=False,
        unique=True,
    )
    responsobility = models.IntegerField("Сила доната", blank=False)
    image = models.ImageField(
        blank=True,
        verbose_name="Изображение доната",
        upload_to="donates/",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Донат"
        verbose_name_plural = "Донаты"


class Profile(AbstractUser):
    profile_image = models.ImageField(
        upload_to="media/profiles/%Y/%m/%d",
        default="media/MinecraftLogo.png",
        verbose_name="Фото пользователя",
    )
    donate = models.ForeignKey(
        "Donate",
        related_name="don",
        verbose_name="Донат пользователь",
        on_delete=models.SET_NULL,
        default=None,
        null=True,
    )

    def get_absolute_url(self):
        return reverse("profile")

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
