from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    CategoryListView,
    CategoryProductView,
    ContactsView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
    UnpublishProductView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path(
        "products/<int:pk>/",
        cache_page(60)(ProductDetailView.as_view()),
        name="product_detail",
    ),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path(
        "products/<int:pk>/unpublish/",
        UnpublishProductView.as_view(),
        name="unpublish_product",
    ),
    path("categories_list/", CategoryListView.as_view(), name="category_list"),
    path(
        "categories/<int:pk>/", CategoryProductView.as_view(), name="category_products"
    ),
]
