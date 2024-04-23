from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "photo", "img_preview", "message", "availability", "created")
    readonly_fields = ["name", "email", "phone", "photo", "img_preview", "message", "availability"]
    list_filter = ("created", )
    search_fields = ("name__startswith", "email__startswith", )
