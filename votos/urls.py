#from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="login"),
    path('eleccion/',views.save_voto,name="eleccion")

]
