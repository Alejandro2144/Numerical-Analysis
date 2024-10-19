from django.urls import path
from .views import *

urlpatterns = [
    
    # Home 
    path('', home_view, name='Home'),

    ##------ urlpatterns for one variable equations ------##

    # {URL} Método de busqueda incremental
    path('incrementalSearch/', incremental_search, name='Busqueda Incremental'),
    # {URL} Método de biseccion
    path('Biseccion/', biseccion, name='Biseccion'),
    # {URL} Método de regla flasa
    path('regla_falsa/', false_rule, name='Regla Falsa'),
    # {URL} Método de punto fijo
    path('punto_fijo/', fixed_point, name='Punto Fijo'),
    
]