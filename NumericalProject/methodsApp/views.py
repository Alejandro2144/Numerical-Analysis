import numpy as np
import matplotlib.pyplot as plt 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .Methods import (
    Busqueda_incremental,
    Biseccion,
    Regla_falsa,
    Punto_fijo,
    Newton_rapshon,
    Secante,
    Raices_multiples,
    Doolittle,
    Crout,
    Cholesky,
    Jacobi,
    Gauss_seidel
)

# -------------------------------------- Homepage --------------------------------------
def home_view(request):
    if request.method == 'GET':
        return render(request, 'Methods/Home.html', {
            'page': 'layouts/nav_bar.html',
            'titulo': 'Home',
            'alerta': 'Ok'
        })
    

# --------------------------------------- Desmos --------------------------------------
def desmos(request):
    if request.method == 'GET':
        return render(request,'Methods/desmos.html',
                              {'titulo': 'Desmos', 'alerta': 'Ok'})
    if request.method == 'POST':
        return render(request, 'Methods/desmos.html',
                      {'titulo': 'Desmos', 'alerta': 'Ok'})

# --------------------------------------- Methods --------------------------------------

# ----------------- One variable equations ----------------

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
    
# ----------------- Systems of equations ----------------

# ---------- Doolittle ----------

def doolittle(request):
    if request.method == 'POST':
        rows = float(request.POST.get('rows'))
        cols = float(request.POST.get('cols'))
        matrix = []
        for i in range(int(rows)):
            row = []
            for j in range(int(cols)):
                val = request.POST.get(f'cell_{i}_{j}')
                row.append(float(val) if val else 0.0)
            matrix.append(row)   
        result = Doolittle.doolittle_function(matrix)
        return render(request, 'Methods/doolittle.html', {'matrix': matrix, 'result': result})
    return render(request, 'Methods/doolittle.html')

# ---------- Crout ----------

def crout(request):
    if request.method == 'POST':
        rows = int(request.POST.get('rows'))
        cols = int(request.POST.get('cols'))
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                val = request.POST.get(f'cell_{i}_{j}')
                row.append(int(val) if val else 0)
            matrix.append(row)
        result = Crout.crout(matrix)
        return render(request, 'Methods/crout.html', {'matrix': matrix, 'result': result})
    return render(request, 'Methods/crout.html')

# ---------- Cholesky ----------

def cholesky(request):
    if request.method == 'POST':
        rows = int(request.POST.get('rows'))
        cols = int(request.POST.get('cols'))
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                val = request.POST.get(f'cell_{i}_{j}')
                row.append(float(val) if val else 0)
            matrix.append(row)
        try:
            result = Cholesky.cholesky(matrix)
            return render(request, 'Methods/Cholesky.html', {'matrix': matrix, 'result': result})
        except ValueError as e:
            error_message = str(e)
            print("Error:", error_message)
            return render(request, 'Methods/Cholesky.html',  {'alerta': 'Fallo', 'mensaje': error_message})
    return render(request, 'Methods/cholesky.html')

# ---------- Jacobi ----------

def jacobi(request):
    if request.method == 'POST':
        try:
            # Obtener el número de filas/columnas
            num_filas = int(request.POST.get('rows'))

            # Obtener valores de la matriz A
            matriz_coeficientes = []
            for i in range(num_filas):
                fila = []
                for j in range(num_filas):
                    val = request.POST.get(f'cell_{i}_{j}')
                    fila.append(float(val) if val else 0.0)
                matriz_coeficientes.append(fila)

            # Obtener valores del vector B
            vector_independiente = [
                float(request.POST.get(f'b_{i}', 0)) for i in range(num_filas)
            ]

            # Obtener valores del vector X0 (vector inicial)
            vector_inicial = [
                float(request.POST.get(f'x0_{i}', 0)) for i in range(num_filas)
            ]

            # Validar tolerancia y número de iteraciones
            try:
                tolerancia = float(request.POST.get('tol'))
                if tolerancia <= 0:
                    raise ValueError("La tolerancia debe ser un número positivo.")
            except ValueError as e:
                return render(
                    request, 
                    'Methods/jacobi.html',
                    {'alerta': 'Fallo', 'mensaje': f"Tolerancia inválida: {str(e)}"}
                )

            iteraciones_maximas = int(request.POST.get('niter'))
            if iteraciones_maximas <= 0:
                return render(
                    request, 
                    'Methods/jacobi.html',
                    {'alerta': 'Fallo', 'mensaje': "El número de iteraciones debe ser mayor que 0"}
                )

            # Ejecutar el método de Jacobi
            html, resultado, iteraciones_realizadas = Jacobi.ejecutar_jacobi(
                matriz_coeficientes, 
                vector_independiente, 
                vector_inicial, 
                tolerancia, 
                iteraciones_maximas
            )

            # Verificar convergencia: matriz diagonalmente dominante o con radio espectral < 1
            if not Jacobi.es_diagonalmente_dominante(np.array(matriz_coeficientes)) and \
               not Jacobi.tiene_radio_espectral_menor_que_uno(np.array(matriz_coeficientes)):
                return render(
                    request, 
                    'Methods/jacobi.html',
                    {
                        'alerta': 'Fallo',
                        'mensaje': 'La matriz no es diagonalmente dominante ni cumple con el radio espectral',
                        'result': resultado,
                        'iteraciones': iteraciones_realizadas
                    }
                )

            # Renderizar resultados si todo está bien
            return render(
                request, 
                'Methods/jacobi.html',
                {'result': resultado, 'iteraciones': iteraciones_realizadas, 'html': html}
            )

        except Exception as e:
            # Mostrar el error en la consola para depuración
            print(f"Error: {e}")
            return render(
                request, 
                'Methods/jacobi.html',
                {'alerta': 'Fallo', 'mensaje': 'Ha ocurrido un error inesperado.'}
            )

    # Renderizar la página inicialmente
    return render(request, 'Methods/jacobi.html')

# ---------- Gauss Seidel ----------

def gauss_seidel(request):
    if request.method == 'POST':
        try:
            # Validar número de filas
            rows = int(request.POST.get('rows'))
            if rows <= 0:
                raise ValueError("El número de filas debe ser mayor que 0.")

            # Obtener y validar la matriz A
            matrix = []
            for i in range(rows):
                row = []
                for j in range(rows):
                    val = request.POST.get(f'cell_{i}_{j}')
                    try:
                        row.append(float(val) if val else 0.0)
                    except ValueError:
                        raise ValueError(f"Valor inválido en la celda {i},{j}")
                matrix.append(row)

            # Obtener y validar el vector B
            vector_b = []
            for i in range(rows):
                val = request.POST.get(f'b_{i}')
                try:
                    vector_b.append(float(val) if val else 0.0)
                except ValueError:
                    raise ValueError(f"Valor inválido en el vector B, posición {i}")

            # Obtener y validar el vector X0
            vector_x0 = []
            for i in range(rows):
                val = request.POST.get(f'x0_{i}')
                try:
                    vector_x0.append(float(val) if val else 0.0)
                except ValueError:
                    raise ValueError(f"Valor inválido en el vector X0, posición {i}")

            # Validar tolerancia y número de iteraciones
            try:
                tol = float(request.POST.get('tol'))
                if tol <= 0:
                    raise ValueError("La tolerancia debe ser mayor que 0.")
            except ValueError:
                return render(request, 'Methods/gausSeidel.html', 
                              {'alerta': 'Fallo', 'mensaje': "Tolerancia inválida"})

            iter = int(request.POST.get('iter'))
            if iter <= 0:
                return render(request, 'Methods/gausSeidel.html', 
                              {'alerta': 'Fallo', 'mensaje': "El número de iteraciones debe ser mayor que 0"})

            # Ejecutar el método de Gauss-Seidel
            result, n, html = Gauss_seidel.Gauss_Seidel(matrix, vector_b, vector_x0, tol, iter)

            # Verificar si la matriz es diagonalmente dominante o cumple con el radio espectral
            if not Gauss_seidel.diagonal_dominante(np.array(matrix)) and not Gauss_seidel.radio_espectral(np.array(matrix)):
                return render(request, 'Methods/gausSeidel.html',
                              {'alerta': 'Fallo', 
                               'mensaje': 'La matriz no es diagonalmente dominante y no cumple con el radio espectral',
                               'result': result, 'iteraciones': n})

            # Mostrar los resultados si todo está bien
            return render(request, 'Methods/gausSeidel.html', 
                          {'result': result, 'iteraciones': n, 'html': html})

        except Exception as e:
            # Mostrar mensaje de error para depuración
            print(f"Error: {e}")
            return render(request, 'Methods/gausSeidel.html', 
                          {'alerta': 'Fallo', 'mensaje': f'Error: {str(e)}'})

    # Renderizar la página inicialmente
    return render(request, 'Methods/gausSeidel.html')
