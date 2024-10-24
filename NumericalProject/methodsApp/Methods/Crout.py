import numpy as np

# En este método, la matriz U tiene unos en su diagonal principal.
# Es decir: U[i,i]=1 para toda i.
# La matriz L contiene los valores en la diagonal y debajo de ella.

def crout(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.eye(n)

    for i in range(n):
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += (L[k][j] * U[j][i])
            L[k][i] = A[k][i] - sum
        for k in range(i, n):
            if i == k:
                U[i][k] = 1
            else:
                sum = 0
                for j in range(i):
                    sum += (L[i][j] * U[j][k])
                U[i][k] = (A[i][k] - sum) / L[i][i]

    return (L, U)
