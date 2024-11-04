from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserRegisterForm
from django.conf import settings
from django.contrib.auth import login
from django.core.mail import send_mail


class RegisterView(CreateView):
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = "Добро пожаловать!"
        message = "Спасибо, что зарегистрировались в нашем магазине!"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user_email]
        send_mail(subject, message, email_from, recipient_list)




# Create your views here.
