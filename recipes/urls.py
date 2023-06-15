from django.urls import path
from . import views

urlpatterns = [

    path("", views.my_home, name="home_site"),  # Home
    path("recipes/<int:id>/", views.recipes, name="recipes"),  # Recipes

]
