from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f'Спасибо, {name}, за Ваше сообщение! Наши специалисты свяжутся с Вами по указанному номеру телефона!')
    return render(request, 'contacts.html')

# Create your views here.
