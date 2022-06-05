from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
]
