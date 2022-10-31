from django.contrib import admin
from .models import Candidato,Persona,Cargo,Lista,Urna,Periodo
# Register your models here.
admin.site.register([Candidato,Persona,Cargo,Lista,Urna,Periodo])
#,Lista,Urna,Periodo])
