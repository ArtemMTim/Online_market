from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "owner",
        "price",
        "image",
        "view_counter",
        "publish_status",
    )
    list_filter = ("category",)
    search_fields = ("title", "description")


# Register your models here.
