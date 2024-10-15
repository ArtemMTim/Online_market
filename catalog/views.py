from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from .models import Product


class ProductListView(ListView):
    model = Product


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

class ProductDetailView(DetailView):
    model = Product
    def get_object(self, queryset=None):
        # Update view counter
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object



class ProductCreateView(CreateView):
    model = Product
    fields = ("title", "description", "price", "image", "category")
    success_url = reverse_lazy('catalog:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/post_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ("title", "description", "price", "image", "category")
    success_url = reverse_lazy('catalog:product_list')
    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


# Create your views here.
