from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from personas.models import Persona


def bienvenido(request):
    no_personas = Persona.objects.count()
    personas = Persona.objects.all()
    return render(request, 'index.html', {'no_personas': no_personas, 'personas': personas})
