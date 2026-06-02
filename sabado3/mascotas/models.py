from django.db import models

# Create your models here.
class Especie(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Especie")
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Propietario(models.Model):
    nombre_completo = models.CharField(max_length=150)
    telefono = models.CharField(max_length= 50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre_completo
    
class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField(help_text="Edad en años")
    fecha_registro = models.DateTimeField(auto_now_add=True)

     # Relaciones (Foreign Keys)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, related_name='mascotas')
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='mascotas')

    def __str__(self):
        return f"{self.nombre} - ({self.especie.nombre})"