import numpy as np
import matplotlib.pyplot as plt 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .Methods import Busqueda_incremental, Biseccion, Regla_falsa, Punto_fijo, Newton_rapshon, Secante, Raices_multiples

# -------------------------------------- Homepage --------------------------------------
def home_view(request):
    if request.method == 'GET':
        return render(request, 'Methods/Home.html', {
            'page': 'layouts/nav_bar.html',
            'titulo': 'Home',
            'alerta': 'Ok'
        })

# --------------------------------------- Methods --------------------------------------

# ---------- Búsqueda Incremental ----------

def incremental_search(request):
    if request.method == 'GET':
        return render(request, 'Methods/busquedaIncremental.html',
                    {'page': 'layouts/nav_bar.html', 'titulo': 'Incremental Search Method', 'alerta': 'Ok'})
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
                    {'page': 'layouts/nav_bar.html', 'titulo': 'Incremental Search Method', 'alerta': 'Ok'})

# ---------- Bisección ----------

def biseccion(request):
    if request.method == 'GET':
        return render(request,'Methods/biseccion.html',
                      {'titulo': 'biseccion', 'alerta': 'Ok'})
    #Valores de entrada: Fx, x0, xi, tol, niter
    if request.method == 'POST' and 'latexinput' in request.POST:
        try:
            expression = request.POST['latexinput']
            tol = float(request.POST['toleranciam'])
            a = float(request.POST['a'])
            b = float(request.POST['b'])
            k = int(request.POST['iteracionm'])
            et = request.POST['tipoe']
        
            tupla = Biseccion.biseccion(expression, a, b, tol, k,et)
            return render(request, 'Methods/biseccion.html',
                          {'page': 'layouts/nav_bar.html', 'expresion': 'Biseccion', 'html': tupla[0], 'mensaje_m': tupla[1]})
        except ValueError as e:
            return render(request, 'Methods/biseccion.html',
                          {'page': 'layouts/nav_bar.html', 'mensaje': e, 'alerta': 'Fallo'})
    else:
        return render(request, 'Methods_Templates/biseccion.html',
                      {'page': 'layouts/nav_bar.html', 'titulo': 'Biseccion', 'alerta': 'Ok'})

# ---------- Regla Falsa ----------

def false_rule(request):
    if request.method == 'GET':
        return render(request,'Methods/reglaFalsa.html',
                      {'page': 'layouts/nav_bar.html', 'titulo': 'False Rule Method', 'alerta': 'Ok'})

    if request.method == 'POST' and 'latexinput' in request.POST:
        try:
            expresion = request.POST['latexinput']
            tol = float(request.POST['toleranciam'])
            a = float(request.POST['ai'])
            b = float(request.POST['bi'])
            k = int(request.POST['iteracionm'])
            et = request.POST['tipoe']

            tupla = Regla_falsa.regla_falsa(expresion, a, b, et, tol, k)
            return render(request, 'Methods/reglaFalsa.html',
                          {'page': 'layouts/nav_bar.html', 'expresion': 'False Rule Method', 'html': tupla[0], 'mensaje_m': tupla[1]})
        except ValueError as e:
            return render(request, 'Methods/reglaFalsa.html',
                          {'page': 'layouts/nav_bar.html', 'mensaje': e, 'alerta': 'Fallo'})
    else:
        return render(request, 'Methods/reglaFalsa.html',
                      {'page': 'layouts/nav_bar.html', 'titulo': 'False Rule Method', 'alerta': 'Ok'})

# ---------- Punto Fijo ----------

def fixed_point(request):
    if request.method == 'GET':
        return render(request,'Methods/puntoFijo.html',
                      {'titulo': 'Punto Fijo', 'alerta': 'Ok'})
    if request.method == 'POST' and 'latexinput' in request.POST:
        try:
            expression = request.POST['latexinput']
            tol = float(request.POST['toleranciam'])
            x0 = float(request.POST['xi'])
            nmax = int(request.POST['iteracionm'])
            et = request.POST['tipoe']

            tupla = Punto_fijo.fixed_point(expression, x0, tol, nmax, et)
            return render(request, 'Methods/puntoFijo.html',
                          {'page': 'layouts/nav_bar.html', 'expression': 'Punto Fijo', 'html': tupla[0], 'mensaje_m': tupla[1]})
        except ValueError as e:
            return render(request, 'Methods/puntoFijo.html',
                          {'page': 'layouts/nav_bar.html', 'mensaje': e, 'alerta': 'Fallo'})
    else:
        return render(request, 'Methods/puntoFijo.html',
                      {'page': 'layouts/nav_bar.html', 'titulo': 'Punto Fijo', 'alerta': 'Ok'})

# ---------- Newton Rapshon ----------

def newton_rapshon(request):
    if request.method == 'GET':
        return render(request, 'Methods/newtonRapshon.html',
                      {'page': 'layouts/nav_bar.html', 'titulo': 'Incremental Search Method', 'alerta': 'Ok'})
    if request.method == 'POST' and 'latexinput' in request.POST:
        try:
            expresion = request.POST['latexinput']
            tol = float(request.POST['toleranciam'])
            a = float(request.POST['ai'])
            k = int(request.POST['iteracionm'])
            et = request.POST['tipoe']

            tupla = Newton_rapshon.newton_rapshon(expresion, a, tol, k, et)
            return render(request, 'Methods/newtonRapshon.html',
                          {'page': 'layouts/nav_bar.html', 'expresion': 'newton Rapshon Method', 'html': tupla[0], 'mensaje_m': tupla[1]})
        except ValueError as e:
            return render(request, 'Methods/newtonRapshon.html',
                          {'page': 'layouts/nav_bar.html', 'mensaje': e, 'alerta': 'Fallo'})
    else:
        return render(request, 'Methods/newtonRapshon.html',
                      {'page': 'layouts/nav_bar.html', 'titulo': 'newton Rapshon Method', 'alerta': 'Ok'})

# ---------- Secante ----------

def secante(request):
    if request.method == 'GET':
        return render(request,'Methods/secante.html',
                      {'titulo': 'secante', 'alerta': 'Ok'})
    #Valores de entrada: Fx, x0, xi, tol, niter
    if request.method == 'POST' and 'latexinput' in request.POST:
        try:
            expression = request.POST['latexinput']
            tol = float(request.POST['toleranciam'])
            x0 = float(request.POST['x0'])
            xi = float(request.POST['xi'])
            k = int(request.POST['iteracionm'])
            et = request.POST['tipoe']
        

            tupla = Secante.secante(expression, xi, x0, tol, k,et)
            return render(request, 'Methods/secante.html',
                          {'page': 'layouts/nav_bar.html', 'expresion': 'Secante', 'html': tupla[0], 'mensaje_m': tupla[1]})
        except ValueError as e:
            return render(request, 'Methods/secante.html',
                          {'page': 'layouts/nav_bar.html', 'mensaje': e, 'alerta': 'Fallo'})
    else:
        return render(request, 'Methods/secante.html',
                      {'page': 'layouts/nav_bar.html', 'titulo': 'Secante', 'alerta': 'Ok'})
    

# ---------- Raices Múltiples ----------

def multiple_roots(request):
    if request.method == 'GET':
        return render(request,'Methods/raicesMultiples.html',
                      {'titulo': 'Raices Multiples', 'alerta': 'Ok'})
    #fx, xi, tol, k, et
    if request.method == 'POST' and 'latexinput' in request.POST:
        try:
            expresion = request.POST['latexinput']
            tol = float(request.POST['toleranciam'])
            xi = float(request.POST['xi'])
            k = int(request.POST['iteracionm'])
            et = request.POST['tipoe']

            tupla = Raices_multiples.multiple_roots(expresion, xi, tol, k, et)
            return render(request, 'Methods/raicesMultiples.html',
                          {'page': 'layouts/nav_bar.html', 'expresion': 'Raices Multiples', 'html': tupla[0], 'mensaje_m': tupla[1]})
        except ValueError as e:
            return render(request, 'Methods/raicesMultiples.html',
                          {'page': 'layouts/nav_bar.html', 'mensaje': e, 'alerta': 'Fallo'})
    else:
        return render(request, 'Methods/raicesMultiples.html',
                      {'page': 'layouts/nav_bar.html', 'titulo': 'Raices Multiples', 'alerta': 'Ok'})