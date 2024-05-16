from django.shortcuts import render, redirect
from .forms import AutorForm, ArticuloForm
from .models import Articulo, Autor


def index(request):
    return render(request, 'blog/index.html')

#READ
def ver_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'blog/ver_articulos.html', {'articulos': articulos})

def ver_autores(request):
    autores = Autor.objects.all()
    return render(request, 'blog/ver_autores.html', {'autores': autores})

# CREATE
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AutorForm()
    return render(request, 'blog/crear_autor.html', {'form': form})

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticuloForm()
    return render(request, 'blog/crear_articulo.html', {'form': form})
