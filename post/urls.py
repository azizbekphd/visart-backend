from django.urls import path

from . import views

urlpatterns = [
    path("new/video/", views.new_video, name="new_video"),
    path("new/image/", views.new_image, name="new_image")
]
