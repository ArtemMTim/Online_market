from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "text", "created_at", "published", "view_counter")
    search_fields = ("title", "published")
    list_filter = ("published",)


# Register your models here.
