from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Загружает данные в БД из фикстур, предварительно очистив БД."

    def handle(self, *args, **options):
        # Очистка БД
        Product.objects.all().delete()
        Category.objects.all().delete()
        # Заполнение БД данными из фикстуры
        call_command("loaddata", "catalog_fixture.json")
        self.stdout.write(
            self.style.SUCCESS("БД успешно заполнена данными из фикстуры")
        )
