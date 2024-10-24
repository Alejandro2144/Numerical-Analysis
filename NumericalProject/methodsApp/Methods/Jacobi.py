import numpy as np
import pandas as pd

def es_diagonalmente_dominante(A):
    """Verifica si la matriz A es diagonalmente dominante."""
    A = np.array(A, dtype=float)
    n = np.shape(A)[0]

    for i in range(n):
        diag = abs(A[i, i])  # Elemento diagonal
        off_diag = sum(abs(A[i, j]) for j in range(n) if i != j)  # Suma de elementos no diagonales
        if diag <= off_diag:
            return False
    return True

def tiene_radio_espectral_menor_que_uno(A):
    """Verifica si el radio espectral de la matriz A es menor que 1."""
    eigvalores = np.linalg.eigvals(A)  # Calcula los eigenvalores
    radio = np.max(np.abs(eigvalores))  # Máximo valor absoluto de los eigenvalores
    return radio < 1

def matriz_sin_infinito_ni_nan(A):
    """Verifica si la matriz A no tiene valores infinitos ni NaN."""
    return not (np.isinf(A).any() or np.isnan(A).any())

def ejecutar_jacobi(A, B, X0, tol, niter):
    """
    Ejecuta el método de Jacobi para resolver un sistema de ecuaciones lineales.
    
    Parámetros:
    - A: Matriz de coeficientes.
    - B: Vector de términos independientes.
    - X0: Vector inicial de aproximación.
    - tol: Tolerancia para la convergencia.
    - niter: Número máximo de iteraciones.

    Retorna:
    - html: Tabla en formato HTML con las iteraciones.
    - resultado: Vector solución.
    - n: Número de iteraciones realizadas.
    """
    df = pd.DataFrame()

    # Convertir A, B y X0 a matrices numpy
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    X0 = np.array(X0, dtype=float)
    
    dimension = np.shape(A)[0]
    X = np.copy(X0)

    n = 0  # Contador de iteraciones
    er = tol + 1  # Error inicial (mayor que la tolerancia)

    # Bucle iterativo del método de Jacobi
    while n < niter and er > tol:
        Xn = np.copy(X)  # Copia del vector actual
        for i in range(dimension):
            suma = sum(A[i, j] * X[j] for j in range(dimension) if j != i)  # Suma de elementos no diagonales
            Xn[i] = (B[i] - suma) / A[i, i]  # Calcular la nueva aproximación para X[i]

        # Calcular el error entre la nueva y la anterior aproximación
        er = np.max(np.abs(np.dot(A, Xn) - B))  
        X = Xn  # Actualizar el vector de aproximaciones
        n += 1  # Incrementar el contador de iteraciones

        # Agregar la iteración al DataFrame
        df = df._append(pd.Series(X, name=n))

    # Crear la tabla con los resultados
    resultado = np.column_stack((np.core.defchararray.add("X", np.arange(1, len(X) + 1).astype(str)), X))
    df.columns = ['X' + str(i + 1) for i in range(dimension)]
    html = df.to_html()  # Convertir el DataFrame a HTML

    return html, resultado, n
