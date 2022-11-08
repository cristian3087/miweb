#from django.http import HttpResponseBadRequest

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
    from django.db.models import Count
    import json
    datos={}
    d = Urna.objects.values('candidato').annotate(count=Count('voto')).order_by()
    print(d)
    can=[]
    res={} 
    datos['resultados']=d
    datos["candidatos"]=candidatos=Candidato.objects.filter(mostrar=True)
    for x in candidatos:
        can.append(x.nombres)
        res[str(x.nombres)]=x.votos()

    can=json.dumps(can)
    res=json.dumps(res)
    print(res)
    datos["res"]=res
    datos["can"] =can
    
    print(can)
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
