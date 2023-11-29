from django.shortcuts import render
from .models import Producto, Categoria

# Create your views here.

def index(request):
    products = Producto.objects.order_by('nombre')
    categoria = Categoria.objects.order_by('nombre')
    context = {'products': products, 'categoria': categoria}
    return render(request, 'index.html', context)

def producto(request):
    productos = Producto.objects.order_by('nombre')
    context = {'products': productos}
    return render(request, 'producto.html', context)

def nosotros(request):
    return render(request, 'nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')