from django.contrib import admin
from .models import Salon, VariableAmbiental
# Register your models here.
@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edificio', 'capacidad', 'largo', 'ancho', 'altura', 'area')
    search_fields = ('nombre', 'edificio')
    list_filter = ('edificio', 'capacidad')
    ordering = ('nombre',)

@admin.register(VariableAmbiental)
class VariableAmbientalAdmin(admin.ModelAdmin):
    list_display = ('salon', 'temperatura', 'humedad', 'iluminacion', 'fecha_registro')
    search_fields = ('salon__nombre',)
    list_filter = ('fecha_registro', 'salon')
    ordering = ('-fecha_registro',)