from django.contrib import admin
from .models import Project, Client, Contact, Subscriber
from django.utils.html import format_html


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "image_thumb")

    def image_thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px; border-radius:4px;" />', obj.image.url)
        return "-"
    image_thumb.short_description = "Image"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "image_thumb")

    def image_thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px; border-radius:50%;" />', obj.image.url)
        return "-"
    image_thumb.short_description = "Photo"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "mobile", "city", "created_at")
    search_fields = ("full_name", "email", "mobile", "city")


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")
    search_fields = ("email",)
