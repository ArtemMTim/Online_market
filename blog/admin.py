from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "published", "view_counter", "slug")
    search_fields = ("title", "published")
    list_filter = ("published",)
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
