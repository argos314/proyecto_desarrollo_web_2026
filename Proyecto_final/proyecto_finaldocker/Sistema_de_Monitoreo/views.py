from django.shortcuts import render
from .models import Salon, VariableAmbiental
# Create your views here.

def lista_salones(request):
    salones = Salon.objects.all()

    return render(request, 'Sistema_monitoreo/lista_salones.html', {'salones': salones})

def lista_variables(request):
    variables = VariableAmbiental.objects.all()

    return render(request, 'variables/lista_variables.html', {'variables': variables})
