from django.urls import path
from .views import *

urlpatterns = [
    
    # Home 
    path('', home_view, name='Home'),

    ##------ urlpattern for graph ------##

    #Url para el metodo grafico
    path('graphing_machine/', graphing_machine, name='Desmos'),

    ##------ urlpatterns for one variable equations ------##

    # {URL} Método de busqueda incremental
    path('incrementalSearch/', incremental_search, name='Busqueda Incremental'),
    # {URL} Método de biseccion
    path('Biseccion/', biseccion, name='Biseccion'),
    # {URL} Método de regla flasa
    path('regla_falsa/', false_rule, name='Regla Falsa'),
    # {URL} Método de punto fijo
    path('punto_fijo/', fixed_point, name='Punto Fijo'),
    # {URL} Método de Newton Rapshon
    path('newton_rapshon/', newton_rapshon, name='Newton Rapshon'),
    # {URL} Método de Secante
    path('secante/', secante, name='Secante'),
    # {URL} Método de Raices Múltiples
    path('raices_multiples/', multiple_roots, name='Raices Multiples'),
    
    ##------ urlpatterns for systems of equations  ------##
    path('doolittle/', doolittle, name='doolittle_matrix'),
]