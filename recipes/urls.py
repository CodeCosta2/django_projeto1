from django.urls import path
from recipes.views import my_home, contact, about

urlpatterns = [

    path("", my_home),  # Home
    path("contato/", contact),  # Contato
    path("sobre/", about)  # Sobre
]
