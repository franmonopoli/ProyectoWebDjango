from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, "ProyectoWebApp/home.html")


def tienda(request):
    return render(request, "ProyectoWebApp/tienda.html")


def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html")