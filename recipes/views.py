from django.shortcuts import render

# Create your views here.


def my_home(request):
    return render(request, 'recipes/pages/home.html')  # Home
