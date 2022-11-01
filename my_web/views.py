#from django.http import HttpResponseBadRequest
import re
from django.shortcuts import render
from votos.models import Persona, Candidato, Urna
def saludo(request):
    data={}
    valor="saludos desde el templates"
    tabla=[]
    for i in range(1,10):
        tabla.append(f"3*{i}={3*i}")
    data["tabla"]=tabla
    data['valor']=valor
    return render(request,'inicio.html',data)

def resultados(request):
    datos={}
    datos["candidatos"]=Candidato.objects.filter(cargo_id=1)
    print("A:",Urna.objects.filter(candidato=1).count())
    print("B:", Urna.objects.filter(candidato=2).count())

    return render(request, 'resultados.html',datos)
def login(request):
    data={}
    if(request.method=="POST"):
        p = Persona.objects.filter(cedula=request.POST['pass'])
        if(p and not Urna.objects.filter(persona_id=p[0].id).exists()):
            data['persona']=p[0]
            print("¿votó?: puede")
            cand = Candidato.objects.all()
            data['candidatos']=cand
            data['title']="Elección 2022"
            
            return render(request, "votos/index.html", data)
        else:
            print("No existe o ya realizo su voto")
            
    return render(request,'login.html')
