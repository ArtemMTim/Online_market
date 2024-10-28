from django import forms
from .models import Product
from django.core.exceptions import ValidationError

STOP_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "image", "category", "price"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название продукта"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )
        self.fields["image"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Укажите изображение продукта"}
        )
        self.fields["category"].widget.attrs.update({"class": "form-control"})
        self.fields["price"].widget.attrs.update({"class": "form-control"})

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if any(word in title.lower() for word in STOP_WORDS):
            raise ValidationError("В названии продукта содержатся запрещенные слова!")
        elif Product.objects.filter(title=title).exists():
            raise ValidationError("Продукт с таким названием уже существует!")
        return title

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if any(word in description.lower() for word in STOP_WORDS):
            raise ValidationError("В описании продукта содержатся запрещенные слова!")
