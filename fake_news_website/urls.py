from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home-page"),
    path("result", views.check, name="result-page"),

    # about page is not yet ready
    path("about", views.about, name="about-page"),
]
