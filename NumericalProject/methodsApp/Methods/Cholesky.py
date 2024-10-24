import numpy as np

# En este método, la matriz A se descompone en:
# A = L ⋅ L^T
# La matriz L es triangular inferior y su transpuesta L^T es triangular superior.
# No hay una matriz U separada, ya que se trabaja únicamente con L y su transpuesta.
# Restricción: Este método solo funciona para matrices simétricas definidas positivas.
# En cada posición diagonal:
# L[i, i] > 0 (valores positivos en la diagonal)

def cholesky(A):
    n = len(A)
    L = np.zeros((n, n))
    transposeA = np.transpose(A)

    if n != len(A[0]):
        raise ValueError("La matriz no es cuadrada")

    if not np.allclose(A, transposeA):
        raise ValueError("La matriz no es simetrica")
    
    if not np.all(np.linalg.eigvals(A) > 0):
        raise ValueError("La matriz no es positiva")
    
    for i in range(n):
        for j in range(i + 1):
            suma = sum(L[i][k] * L[j][k] for k in range(j))

            if i == j: # elementos de la diagonal
                sqrt_term = A[i][i] - suma
                #if sqrt_term < 0:
                #    raise ValueError("La matriz no es definida positiva.")
                L[i][j] = np.sqrt(sqrt_term)
            else: # Elementos fuera de la diagonal
                L[i][j] = (1.0 / L[j][j] * (A[i][j] - suma))
    return L