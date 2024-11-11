from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import ProductForm
from .models import Category, Product
from .service import category_products, get_product_list


class CategoryListView(ListView):
    """Контроллер отображения списка категорий продуктов."""

    model = Category
    template_name = "catalog/category_list.html"


class ProductListView(ListView):
    """Контроллер отображения списка всех опубликованных продуктов."""

    model = Product

    def get_queryset(self):
        return get_product_list()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["published_products"] = Product.objects.filter(publish_status=True)
        return context


class ContactsView(TemplateView):
    """Контроллер отображения страницы контактов."""

    template_name = "catalog/contacts.html"


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Контроллер отображения деталей о продукте."""

    model = Product
    login_url = reverse_lazy("users:login")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создания продукта."""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")
    login_url = reverse_lazy("users:login")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер удаления продукта."""

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if (
            not self.request.user.has_perm("delete_product")
            or self.request.user != product.owner
        ):
            return HttpResponseForbidden("У вас нет прав на это действие.")

    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер изменения продукта."""

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if self.request.user != product.owner:
            return HttpResponseForbidden("У вас нет прав на это действие.")

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")
    login_url = reverse_lazy("users:login")

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


class UnpublishProductView(LoginRequiredMixin, View):
    """Контроллер снятия продукта с публикации на главной странице"""

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if not request.user.has_perm("can_unpublish_product"):
            return HttpResponseForbidden("У вас нет прав на это действие.")

        product.publish_status = False
        product.save()
        return redirect("catalog:product_list")


class CategoryProductView(LoginRequiredMixin, ListView):
    """Контроллер отображения всех продуктов в отдельной категории."""

    template_name = "catalog/category_product.html"
    context_object_name = "products"
    login_url = reverse_lazy("users:login")

    def get_queryset(self):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        print(pk)
        return category_products(pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = self.get_queryset()
        return context


# Create your views here.
