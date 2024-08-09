from django.contrib import admin
from user.models import Profile, Donate


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "profile_image", "donate"]
    list_editable = ["first_name", "profile_image", "username"]
    list_display_links = ["donate"]
    # ordering = ["donate"]
    search_fields = ["username"]
    list_filter = ["donate__name"]


@admin.register(Donate)
class DonateAdmin(admin.ModelAdmin):
    list_display = ["name", "responsobility", "image"]
    list_display_links = ["responsobility"]
    list_editable = ["name"]
    ordering = ["-responsobility"]
    search_fields = ["name"]
