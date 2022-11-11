from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Candidato, Urna, Persona,Wiki
from .forms import WikiForm
# Create your views here.
def index(request):

    return render(request,"index.html")

def save_voto(request):
    print(request.GET)
    urna=Urna(persona_id=request.GET['u'],candidato_id=request.GET['c'],voto=True)
    urna.save()
    return HttpResponseRedirect('/')

def wiki(request):
    
    data={}
    form=WikiForm(request.POST)
    if request.method == 'POST':
        try:
            if form.is_valid():
                print("POST:",request.POST['id'])
                wiki=None
                if request.POST['id']:
                    wiki=Wiki.objects.get(id=request.POST['id'])
                    wiki.title=form.cleaned_data['title']
                    wiki.data=form.cleaned_data['data']
                else:
                    wiki=Wiki(title=form.cleaned_data['title'],data=form.cleaned_data['data'])
                wiki.save()
                return HttpResponseRedirect('/votos/wiki')
                #return redirect('/')
        except Exception as ex:
            print(ex)
        return HttpResponseRedirect('/')    
    else:   
        form=WikiForm() 
        id=None
        if 'id' in request.GET:
            wiki=Wiki.objects.get(pk=request.GET['id'])
            print('wiki:', wiki,Wiki.objects.all())            
            form=WikiForm(initial={
                'title':wiki.title,
                'data':wiki.data
            })
            print(request.GET['id'])
            id=request.GET['id']
        data['id']=id    
        data['form']=form
        data['wikis']= Wiki.objects.all()
        print(request.method)
       # print(request['GET'])
        data['form']= form
        return render(request,"votos/wiki.html",data)
