from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.index, name='index'),
    path('crear_autor/', views.crear_autor, name='crear_autor'),
    path('crear_articulo/', views.crear_articulo, name='crear_articulo'),
    path('ver_autores/', views.ver_autores, name='ver_autores'),
    path('ver_articulos/', views.ver_articulos, name='ver_articulos'),
]
