from django.contrib import admin

# Register your models here.
from .models import Especie, Propietario, Mascota

# Registramos el modelo Especie de forma simple
@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

# Registramos el modelo Propietario de forma simple
@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'telefono', 'email')
    search_fields = ('nombre_completo', 'email')

# Registramos Mascota con filtros y búsqueda avanzada
@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'propietario', 'edad', 'fecha_registro')
    list_filter = ('especie',) # Agrega un panel de filtros lateral
    search_fields = ('nombre', 'propietario__nombre_completo') # Busca por nombre de mascota o del dueño
    ordering = ('-fecha_registro',) # Ordena de las más recientes a las más antiguas