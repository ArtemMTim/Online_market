from django.core.cache import cache

from catalog.models import Category, Product
from config.settings import CACHE_ENABLED


def get_product_list():
    """Работает с кэш при просмотре всех продуктов.
    Записывает и достаёт из кэш."""
    if not CACHE_ENABLED:
        return Product.objects.all().filter(publish_status=True)
    else:
        key = "product_list"
        products = cache.get(key)
        if products is not None:
            return products
        else:
            products = Product.objects.all().filter(publish_status=True)
            cache.set(key, products, 60)  # Cache for 1 hour
            return products


def category_products(pk):
    """Принимает pk категории. Возвращает все продукты в указанной категории."""
    category = Category.objects.get(pk=pk)
    products = Product.objects.all().filter(category=category)
    return products
