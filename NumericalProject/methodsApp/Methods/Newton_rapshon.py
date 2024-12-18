import pandas as pd
from latex2sympy2 import latex2sympy
import sympy

def newton_rapshon(fx: str, a: float, tol: float, k: int, et: str) -> tuple:
    tabla = pd.DataFrame(columns=['x', 'f(x)', 'Error'])
    
    try:
        sympy_exp = latex2sympy(fx)
        fn = sympy.sympify(sympy_exp)
        df = sympy.diff(fn)
    except:
        raise ValueError('La funcion no es valida')
    
    x = a
    Iterations = 0
    
    while Iterations < k:
        # Calculate valor de la derivada
        y_prime = df.subs({'x': x})

        # Verificar si la derivada es muy cercana a cero
        if sympy.Abs(y_prime) < 0.00000009:
             raise ValueError('La derivada de la funcion es muy cercana a cero')

        # Calculamos valor de la funcion
        x_act = fn.subs({'x': x})

        # Calculamos la siguiente aproximacion utilizando el metodo de Newton
        x_next = x - x_act / y_prime

        # Calculamos el error
        if et == 'Correct decimals':
            error = sympy.Abs(x_next - x)
        elif et == 'Significant figures':
            error = sympy.Abs((x_next - x) / x)
        else:
            raise ValueError('Error en error')

        # Agregar una fila al DataFrame
        tabla.loc[len(tabla)] = [x, x_act, error]

        # Actualizamos la aproximacion para la siguiente iteracion
        x = x_next
        Iterations += 1

        if error < tol:
            break
    
    html = tabla.to_html()

    if Iterations >= k:
        return (html, 'El metodo fallo en {} Iterations'.format(k))
    else:
        return (html, f'El metodo convergio a la solucion en la iteración {Iterations}')
