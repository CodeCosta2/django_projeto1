# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def my_home(request):
    return HttpResponse('Home 1...2...3')


def contact(request):
    return HttpResponse('Contato 1...2...3')


def about(request):
    return HttpResponse('Sobre 1...2...3')
