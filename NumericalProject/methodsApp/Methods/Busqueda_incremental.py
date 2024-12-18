import pandas as pd
from latex2sympy2 import latex2sympy
import sympy
import math

def busqueda_incremental(fx: str, a: float, tol: float, k: int):
    tabla = pd.DataFrame(columns=['Intervalo con raices'])

    try:
        sympy_exp = latex2sympy(fx)
        fn = sympy.sympify(sympy_exp)
        fa = fn.subs({'x': a})
        fa = fa.evalf()
        if math.isnan(fa):
            raise ValueError('La función no es válida')
    except:
        raise ValueError('La función no es válida')
    
    x1 = a
    x2 = x1 + tol
    Iterations = 0

    while Iterations <= k:
        y1 = fn.subs({'x': x1})
        y2 = fn.subs({'x': x2})

        #Si los signos son opuestos, hay raiz
        if (y1 < 0 and y2 >= 0) or (y1 >= 0 and y2 < 0):
            nuevo_dataframe = pd.DataFrame({'Intervalo con raices': [f"[{x1}, {x2}]"]})
            tabla = pd.concat([tabla, nuevo_dataframe], ignore_index=True)
            
            break
        
        x1 = x2
        x2 = x1 + tol
        Iterations += 1
    html = tabla.to_html()
    
    if tabla.empty:
        return (html, f'El método falló en {Iterations} Iterations')
    else:
        return (html, f'El método convergió a la solución en {Iterations} Iterations')
