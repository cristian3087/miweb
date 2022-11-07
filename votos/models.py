from email.policy import default
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Persona(models.Model):
    cedula=models.CharField(default='', max_length=10,verbose_name='cedula')
    nombres=models.CharField(max_length=50,verbose_name="nombres")
    apellidos=models.CharField(max_length=70,verbose_name="apellidos")
    #usuario=models.ForeignKey(User, null=True, verbose_name='usuario',on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nombres
    

class Cargo(models.Model):
    nombre=models.CharField(verbose_name="Cargo", max_length=30)
    fecha=models.DateField(auto_now_add=True)
    descripcion=models.TextField(verbose_name="Descripcion",null=True,blank=True)
    def __str__(self) -> str:
        return self.nombre


class Lista(models.Model):
    nombre=models.CharField(verbose_name="Nombre Lista",max_length=40)
    alias=models.CharField(verbose_name="Alias", max_length=30)
    def __str__(self) -> str:
        return self.nombre

class Periodo(models.Model):
    nombre = models.CharField(default='', max_length=200, verbose_name=u'Nombre')
    alias = models.CharField(default='', max_length=200, verbose_name=u'Nombre')
    inicio = models.DateField(verbose_name=u'Fecha inicio')
    fin = models.DateField(verbose_name=u'Fecha fin')
    activo = models.BooleanField(default=True, verbose_name=u'Visible')
    def __str__(self) -> str:
        return self.nombre


class Candidato(models.Model):
    periodo=models.ForeignKey(Periodo, verbose_name='Periodo' , on_delete=models.CASCADE)
    #persona=models.ForeignKey(Persona, verbose_name='Candidato', on_delete=models.CASCADE)
    nombres = models.CharField(default='',max_length=200,verbose_name='Nombres')
    apellidos = models.CharField(default='',max_length=200,verbose_name='Apellidos',blank=True)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d', verbose_name=u'Foto', blank=True, null=True)
    cargo = models.ForeignKey(Cargo,verbose_name="Cargo", on_delete=models.CASCADE)
    lista = models.ForeignKey(Lista,verbose_name="Lista", on_delete=models.CASCADE)
    mostrar = models.BooleanField(default=False, verbose_name='Mostrar')
    def __str__(self) -> str:
        return self.nombres + ' '+ self.apellidos

    def votos(self):
        return Urna.objects.filter(candidato=self.id).count()



class Urna(models.Model):
    persona=models.ForeignKey(Persona, verbose_name="persona", on_delete=models.CASCADE)
    candidato=models.ForeignKey(Candidato, verbose_name="candidato", on_delete=models.CASCADE)
    voto= models.BooleanField(default=False,verbose_name="voto")
    
    def __str__(self) -> str:
        return self.candidato.nombres


    
