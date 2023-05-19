from django.shortcuts import render

# Create your views here.


def my_home(request):
    return render(request, 'recipes/home.html')


def contact(request):
    return render(request, 'recipes/contato.html')


def about(request):
    return render(request, 'recipes/sobre.html')
