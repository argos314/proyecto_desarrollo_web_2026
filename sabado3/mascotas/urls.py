from django.urls import path
from . import views

urlpatterns = [
    # Ruta vacía ('') significa la página principal de esta app
    path('', views.lista_mascotas, name='lista_mascotas'),
]


