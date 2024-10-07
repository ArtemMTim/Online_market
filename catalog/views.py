from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "home.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            f"Спасибо, {name}, за Ваше сообщение! Наши специалисты свяжутся с Вами по указанному номеру телефона!"
        )
    return render(request, "contacts.html")

def product_details(request):
    product = Product.objects.get(id=1)
    context = {'product': product}
    return render(request, "product_details.html", context)



# Create your views here.
