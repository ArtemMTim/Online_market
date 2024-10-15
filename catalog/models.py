from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=150, verbose_name="Название", help_text="Введите название категории"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Введите описание категории",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["title"]


class Product(models.Model):
    title = models.CharField(
        max_length=150, verbose_name="Название", help_text="Введите название продукта"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Введите описание продукта",
    )
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Изображение",
        blank=True,
        null=True,
        help_text="Загрузите фотографию продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория",
    )
    view_counter = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")
    price = models.FloatField(verbose_name="Цена", help_text="Введите цену продукта")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.title} {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["title"]


# Create your models here.
