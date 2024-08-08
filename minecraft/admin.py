from django.contrib import admin
from minecraft.models import News, Servers


# Register your models here.
@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ["title", "text", "slug", "is_published", "server"]
    list_display_links = ["server"]
    list_editable = ["title", "text", "is_published"]


@admin.register(Servers)
class AdminServers(admin.ModelAdmin):
    list_display = ["max_online", "slug"]
    list_editable = ["slug"]
