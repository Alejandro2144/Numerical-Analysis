from latex2sympy2 import latex2sympy
import pandas as pd
import sympy
import math

def secante(fx: str, xi: float, x0: float, tol: float, niter: int, et: str) -> tuple:
    tabla = pd.DataFrame(columns=['Iterations', 'Xi', 'f(xi)', 'Error'])

    try:
        # Interpretar la función desde LaTeX a SymPy
        sympy_exp = latex2sympy(fx)
        fn = sympy.sympify(sympy_exp)

        # Evaluar f(x) en los puntos iniciales
        fi = fn.subs({'x': xi}).evalf()
        f0 = fn.subs({'x': x0}).evalf()
    except Exception as e:
        raise ValueError(f'La función no es válida: {e}')

    # Validar si f(x0) y f(xi) son iguales para evitar división por cero
    if math.isclose(f0, fi, abs_tol=1e-12):
        raise ValueError('Los valores iniciales producen una división por cero.')

    # Registrar las dos primeras Iterations
    tabla = tabla._append({'Iterations': 0, 'Xi': x0, 'f(xi)': f0, 'Error': ""}, ignore_index=True)
    tabla = tabla._append({'Iterations': 1, 'Xi': xi, 'f(xi)': fi, 'Error': ""}, ignore_index=True)

    n = 2  # Contador de Iterations
    er = tol + 1  # Inicialización del error para entrar al ciclo

    # Bucle de iteración
    while n <= niter and er > tol:
        # Validar si f0 y fi son muy cercanos para evitar la división por cero
        if math.isclose(f0 - fi, 0, abs_tol=1e-12):
            raise ValueError('División por cero detectada en el cálculo de la secante.')

        # Calculate la nueva aproximación usando la fórmula de la secante
        try:
            xm = xi - (fi * (x0 - xi) / (f0 - fi))
        except ZeroDivisionError:
            raise ValueError('División por cero detectada.')

        fxm = fn.subs({'x': xm}).evalf()

        # Verificar si la función devuelve NaN
        if math.isnan(fxm):
            raise ValueError('La función devolvió NaN durante la iteración.')

        # Calculate el error basado en el tipo especificado
        if et == 'Correct decimals':
            er = sympy.Abs(xm - xi)
        elif et == 'Significant figures':
            er = sympy.Abs((xm - xi) / xm)
        else:
            raise ValueError('Error en el Type of error.')

        # Registrar la iteración en la tabla
        tabla = tabla._append({'Iterations': n, 'Xi': xm, 'f(xi)': fxm, 'Error': er}, ignore_index=True)

        # Actualizar valores para la siguiente iteración
        x0, xi = xi, xm
        f0, fi = fi, fxm
        n += 1

    # Convertir la tabla a HTML para mostrarla en el frontend
    html = tabla.to_html()

    # Verificar si el método convergió o falló
    if er < tol:
        return html, f'El método convergió a la solución {xm} en {n - 1} Iterations'
    else:
        return html, f'El método falló en {niter} Iterations'
