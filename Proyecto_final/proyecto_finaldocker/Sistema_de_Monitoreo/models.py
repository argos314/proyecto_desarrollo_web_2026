from django.db import models

class Salon(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Salon")
    edificio = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    largo = models.FloatField()
    ancho = models.FloatField()
    altura = models.FloatField()

    def area(self):
        return self.largo * self.ancho
    area.short_description = "Area (m2)"

    def __str__(self):
        return self.nombre

class VariableAmbiental(models.Model):
    temperatura = models.FloatField()
    humedad = models.FloatField()
    iluminacion = models.FloatField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

 # Relaciones (Foreign Keys)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE,)

    def __str__(self):
        return f"{self.salon.nombre}"
