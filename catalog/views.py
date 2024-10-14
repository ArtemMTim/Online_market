from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Product


class ProductListView(ListView):
    model = Product

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            f"Спасибо, {name}, за Ваше сообщение! Наши специалисты свяжутся с Вами по указанному номеру телефона!"
        )
    return render(request, "contacts.html")


class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    fields = ("title", "description", "price", "image", "category")
    success_url = reverse_lazy('catalog:product_list')

# Create your views here.
