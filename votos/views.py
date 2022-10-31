from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Candidato, Urna, Persona
# Create your views here.
def index(request):

    return render(request,"index.html")

def save_voto(request):
    print(request.GET)
    urna=Urna(persona_id=request.GET['u'],candidato_id=request.GET['c'],voto=True)
    urna.save()
    return HttpResponseRedirect('/')
