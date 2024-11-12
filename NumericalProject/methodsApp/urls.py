from django.urls import path
from .views import *

urlpatterns = [
    
    # Home 
    path('', home_view, name='Home'),

    ##------ urlpattern for desmos ------##

    #Url para el metodo grafico
    path('desmos/', desmos, name='Desmos'),

    ##------ urlpatterns for one variable equations ------##

    # {URL} Método de LU Simple Gauss
    path('lu_simple_gaussiana/', lu_simple_gaussiana, name='lu_simple_gaussiana'),
    # {URL} Método de Guassian con pivoteo
    path('gaussian_pivoting/', gaussian_pivoting, name='gaussian_pivoting'),
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

    # {URL} Método de Doolittle
    path('doolittle/', doolittle, name='doolittle_matrix'),
    # {URL} Método de Crout
    path('crout/', crout, name='crout_matrix'),
    # {URL} Método de Cholesky
    path('cholesky/', cholesky, name='cholesky_matrix'),
    # {URL} Método de Jacobi
    path('jacobi/', jacobi, name='Jacobi'),
    # {URL} Método de Gauss Seidel
    path('gauss_seidel/', gauss_seidel, name='gauss_seidel_matrix'),
]