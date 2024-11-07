from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import ProductForm
from .models import Product


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["published_products"] = Product.objects.filter(publish_status=True)
        return context


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    login_url = reverse_lazy("users:login")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
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
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if not request.user.has_perm("can_unpublish_product"):
            return HttpResponseForbidden("У вас нет прав на это действие.")

        product.publish_status = False
        product.save()
        return redirect("catalog:product_list")


# Create your views here.
