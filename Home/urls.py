from django.urls import path
from .views  import Home,ContactForm

urlpatterns = [
    path("", Home , name="home"),
    path("contact/", ContactForm , name="contatc")
]
