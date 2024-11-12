import numpy as np

# En este método, la matriz L tiene unos en su diagonal principal.
# Es decir: L[i, i] = 1 para todo i.
# La matriz U tiene los valores por encima y en la diagonal principal.

def lu_simple_gaussiana(A):
    n = len(A)
    L = np.eye(n)  # Inicializa la matriz L como una matriz identidad
    U = np.zeros((n, n))  # Inicializa la matriz U con ceros
    A = np.array(A, dtype=float)  # Asegurarse de que A es de tipo float

    for k in range(n):
        # Verificar que el elemento diagonal no sea cero
        if A[k][k] == 0:
            raise ValueError("El elemento diagonal es cero. No se puede continuar con la eliminación gaussiana.")
        # Construir la matriz U
        for j in range(k, n):
            U[k][j] = A[k][j]
        # Construir la matriz L y modificar A
        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            L[i][k] = factor
            for j in range(k, n):
                A[i][j] = A[i][j] - factor * A[k][j]
    return (L, U)

# Función para resolver el sistema LUx = b
def resolve_lu(L, U, b):
    n = len(L)
    y = np.zeros(n)
    x = np.zeros(n)

    # Sustitución hacia adelante Ly = b
    for i in range(n):
        sumatoria = sum(L[i][j] * y[j] for j in range(i))
        y[i] = b[i] - sumatoria

    # Sustitución hacia atrás Ux = y
    for i in range(n-1, -1, -1):
        sumatoria = sum(U[i][j] * x[j] for j in range(i+1, n))
        if U[i][i] == 0:
            raise ValueError("La matriz U tiene un cero en la diagonal.")
        x[i] = (y[i] - sumatoria) / U[i][i]

    return x