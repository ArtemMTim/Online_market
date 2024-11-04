from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text", "image", "published"]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название поста"}
        )
        self.fields["text"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите текст поста"}
        )
        self.fields["image"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Укажите изображение для поста"}
        )
        self.fields["published"].widget.attrs.update({"class": "form-check-input"})

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if Post.objects.filter(title=title).exists():
            raise ValidationError(
                "Пост с таким название уже существует! Выберите новое название."
            )
        return title
