from django.db import models

class Post(models.Model):
    title = models.CharField(
        max_length=150, verbose_name="Заголовок", help_text="Введите название категории"
    )
    text = models.TextField(
        verbose_name="Текст поста",
        blank=True,
        null=True,
        help_text="Введите текст поста",
    )
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Изображение",
        blank=True,
        null=True,
        help_text="Загрузите фотографию к посту",
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    published = models.BooleanField(default=False, verbose_name="Признак публикации")
    view_counter = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        ordering = ["title"]

# Create your models here.
