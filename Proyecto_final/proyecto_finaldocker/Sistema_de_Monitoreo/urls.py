from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_salones, name= 'lista_salones'),
    path('variables/', views.lista_variables, name='lista_variables'),
]