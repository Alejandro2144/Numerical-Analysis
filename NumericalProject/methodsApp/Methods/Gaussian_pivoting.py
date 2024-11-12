import numpy as np

def partialPivot(Ab, k):
    """
    Realiza el pivoteo parcial en la matriz aumentada Ab en la columna k.
    Intercambia filas si es necesario para que el elemento pivote tenga el mayor valor absoluto.
    """
    # Encuentra el índice de la fila con el mayor valor absoluto en la columna k desde la fila k en adelante
    max_index = np.argmax(np.abs(Ab[k:, k])) + k

    # Verifica si se necesita realizar un intercambio
    if max_index != k:
        # Intercambia las filas k y max_index
        Ab[[k, max_index]] = Ab[[max_index, k]]
    
    return Ab

def partialPivotElimination(Ab, n):
    """
    Realiza la eliminación gaussiana con pivoteo parcial en la matriz aumentada Ab.
    """
    for k in range(n):
        Ab = partialPivot(Ab, k)
        for i in range(k + 1, n):
            if Ab[k, k] == 0:
                raise ValueError("División por cero: la eliminación gaussiana no es posible.")
            
            # Calcula el multiplicador para la eliminación
            multiplier = Ab[i, k] / Ab[k, k]

            # Aplica la eliminación fila por fila, de k hasta el final
            Ab[i, k:] -= multiplier * Ab[k, k:]
    
    return Ab

def regSus(Ab, n):
    """
    Realiza la sustitución hacia atrás para resolver el sistema después de la eliminación gaussiana.
    """
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if Ab[i, i] == 0:
            raise ValueError("Sistema no tiene solución única.")
        # Calcula cada valor de x[i] usando la sustitución hacia atrás
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:n])) / Ab[i, i]
    return x

def gausPartialPivot(A, b):
    """
    Aplica el método de eliminación gaussiana con pivoteo parcial para resolver el sistema Ax = b.
    """
    # Combina A y b en una matriz aumentada Ab
    Ab = np.hstack((A, b.reshape(-1, 1)))
    n = len(b)
    
    # Aplica eliminación gaussiana con pivoteo parcial
    Ab = partialPivotElimination(Ab, n)
    
    # Realiza sustitución hacia atrás para obtener la solución final
    x = regSus(Ab, n)
    
    return x
