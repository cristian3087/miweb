from django.shortcuts import render
from .models import Candidato
# Create your views here.
def index(request):
    cand= Candidato.objects.all()
    data={}
    data['candidatos']=cand
    data['saludo']="Hola este es un salulo"
    return render(request,"votos/index.html",data)