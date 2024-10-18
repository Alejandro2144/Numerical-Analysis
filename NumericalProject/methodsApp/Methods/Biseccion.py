from latex2sympy2 import latex2sympy
import pandas as pd
import sympy

def biseccion(fx: str, a: float, b: float, tol: float, niter: int, et: str) -> tuple:
    registros = []  # Lista para almacenar las iteraciones

    sympy_exp = latex2sympy(fx)
    fn = sympy.sympify(sympy_exp)

    fa = fn.subs({'x': a}).evalf()
    fb = fn.subs({'x': b}).evalf()

    if fa * fb > 0:
        raise ValueError('La función debe cambiar de signo en el intervalo.')

    if et == 'Decimales Correctos':
        er = sympy.Abs(b - a)
    elif et == 'Cifras Significativas':
        if a == 0:
            raise ValueError("El valor de 'a' no puede ser 0 para evitar divisiones por 0")
        er = sympy.Abs((b - a) / a)
    else:
        raise ValueError('Tipo de error no reconocido.')

    i = 1
    c = a  # Inicializa el punto medio

    while er > tol and i <= niter:
        c = (a + b) / 2
        fc = fn.subs({'x': c}).evalf()

        if fc == 0 or sympy.Abs(fc) < tol:
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        if et == 'Decimales Correctos':
            er = sympy.Abs(b - a)
        elif et == 'Cifras Significativas':
            if a == 0:
                raise ValueError("El valor de 'a' no puede ser 0 para evitar divisiones por 0.")
            er = sympy.Abs((b - a) / a)

        registros.append({'Iteraciones': i, 'a': a, 'b': b, 'f(c)': fc, 'Error': er})
        i += 1

    tabla = pd.DataFrame(registros)
    html = tabla.to_html()
    return html, f'El método convergió a la solución {c}.'
