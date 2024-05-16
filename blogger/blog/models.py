from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    apellido = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100,)
    github = models.CharField(max_length=100,)
    whatsapp = models.IntegerField()

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    contenido = models.TextField(max_length=1000, null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    