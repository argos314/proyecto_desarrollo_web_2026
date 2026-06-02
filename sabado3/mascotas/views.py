from django.shortcuts import render

# Create your views here.
from .models import Mascota

def lista_mascotas(request):
    # Obtenemos todas las mascotas de la base de datos, ordenadas por la más reciente
    todas_las_mascotas = Mascota.objects.all().order_by('-fecha_registro')
    
    # Preparamos un "contexto" (un diccionario) para enviarlo a la plantilla HTML
    contexto = {
        'mascotas': todas_las_mascotas
    }
    
    # Renderizamos la plantilla enviándole los datos
    return render(request, 'mascotas/lista_mascotas.html', contexto)