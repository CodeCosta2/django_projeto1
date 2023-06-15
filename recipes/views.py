from django.shortcuts import render

# Create your views here.


def my_home(request):
    return render(request, 'recipes/pages/home.html')  # Home


def recipes(request, id):
    return render(request, 'recipes/pages/recipe-view.html')  # Recipes
