from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView

from users.apps import UsersConfig


app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path(
        "register/",
        RegisterView.as_view(template_name="register.html"),
        name="register",
    ),
]
