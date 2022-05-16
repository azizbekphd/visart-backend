from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("signin/", views.login, name="signin"),
    path("signup/", views.login, name="signup"),
]
