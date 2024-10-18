from latex2sympy2 import latex2sympy
import pandas as pd
import sympy
import math

def regla_falsa(fx: str, a: float, b: float, et: bool, tol: float, k: int) -> tuple:
    """
    Implementación del método de Regla Falsa para encontrar raíces.

    Args:
        fx: Cadena en formato LaTeX con la función a evaluar.
        a: Cota inferior del intervalo donde se busca la raíz.
        b: Cota superior del intervalo donde se busca la raíz.
        et: Bandera para indicar el tipo de error (no se usa en esta implementación).
        tol: Tolerancia del error.
        k: Número máximo de iteraciones.

    Returns:
        Una tupla con el HTML de la tabla y un mensaje sobre la convergencia.
    """
    registros = []  # Lista para almacenar los registros de las iteraciones.

    # Parseo y validación de la función.
    try:
        sympy_exp = latex2sympy(fx)
        fn = sympy.sympify(sympy_exp)
        fa = fn.subs({'x': a}).evalf()
        fb = fn.subs({'x': b}).evalf()

        if math.isnan(fa) or math.isnan(fb):
            raise ValueError('La función no es válida.')
    except Exception as e:
        raise ValueError(f'Error al interpretar la función: {e}')

    # Verificación de cambio de signo en el intervalo.
    if fa * fb > 0:
        raise ValueError('No hay raíz en el intervalo.')
    if fa == 0 or fb == 0:
        raise ValueError('Uno de los extremos es una raíz exacta.')

    error = tol + 1  # Inicialización del error para entrar al ciclo.
    xm_1 = 0  # Valor anterior de xm.
    n = 0  # Contador de iteraciones.

    # Ciclo principal del método.
    while error > tol and n < k:
        xm = (a * fb - b * fa) / (fb - fa)  # Fórmula de Regla Falsa.
        fxm = fn.subs({'x': xm}).evalf()  # Evaluación en el nuevo punto.

        # Actualización del intervalo según el signo del producto.
        if fa * fxm < 0:
            b = xm
            fb = fxm
        else:
            a = xm
            fa = fxm

        # Cálculo del error si no es la primera iteración.
        if n > 0:
            error = abs(xm - xm_1)
        xm_1 = xm

        # Almacena los resultados de la iteración.
        registros.append({'Valor de a': a, 'Valor de b': b, 'Valor de xm': xm, 'Error': error})
        n += 1

    # Genera la tabla en formato HTML.
    tabla = pd.DataFrame(registros)
    html = tabla.to_html()

    # Verifica si el método logró converger.
    if n >= k:
        return html, f'El método falló en {k} iteraciones'
    else:
        return html, f'El método convergió a la solución {xm} con un error menor a {tol}'