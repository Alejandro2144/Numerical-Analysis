import numpy as np
import matplotlib.pyplot as plt 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .Methods import Busqueda_incremental

# -------------------------------------- Homepage --------------------------------------
def home_view(request):
    if request.method == 'GET':
        return render(request, 'Methods/Home.html', {
            'page': 'layouts/nav_bar.html',
            'titulo': 'Home',
            'alerta': 'Bien'
        })

# --------------------------------------- Methods --------------------------------------

def incremental_search(request):
    if request.method == 'GET':
        return render(request, 'Methods/busquedaIncremental.html',
                      {'page': 'layouts/nav_bar.html', 'titulo': 'Incremental Search Method', 'alerta': 'Melo'})
    if request.method == 'POST' and 'latexinput' in request.POST:
        try:
            expresion = request.POST['latexinput']
            tol = float(request.POST['toleranciam'])
            a = float(request.POST['ai'])
            #b = float(request.POST['bi'])
            k = int(request.POST['iteracionm'])
            #et = request.POST['tipoe']

            tupla = Busqueda_incremental.busqueda_incremental(expresion, a, tol, k)
            return render(request, 'Methods/busquedaIncremental.html',
                          {'page': 'layouts/nav_bar.html', 'expresion': 'Incremental Search Method', 'html': tupla[0], 'mensaje_m': tupla[1]})
        except ValueError as e:
            return render(request, 'Methods/busquedaIncremental.html',
                          {'page': 'layouts/nav_bar.html', 'mensaje': e, 'alerta': 'Fallo'})
    else:
        return render(request, 'Methods/busquedaIncremental.html',
                      {'page': 'layouts/nav_bar.html', 'titulo': 'Incremental Search Method', 'alerta': 'Melo'})