import sys

def power_of_two(n):
    return (n != 0) and (n & (n-1) == 0)  #forma eficiente de verificar si un número n es una potencia de 2 en programación.

def hadamard(matrix, n):
    if n == 1:
        return matrix[0][0]           #Caso base primera fila primera columna
    for i in range(n):
        for j in range(i+1, n):
            if sum(matrix[i][k] != matrix[j][k] for k in range(n)) != n/2:   # los elementos de cada dos filas
                # adyacentes difieren exactamente en n/2 elementos
                return False
    return True

def check_hadamard(n, values):
    if not power_of_two(n):
        return "Imposible"
    matrix = crear_matriz(n)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = values[i*n+j] == 'T'
    return "Hadamard" if hadamard(matrix, n) else "No Hadamard"

def crear_matriz(tam):
    matriz = [[False]*tam for _ in range(tam)]                 #False porque se llena con valores booleanos
    return matriz

for line in sys.stdin:
    n = int(line)
    values = next(sys.stdin).split()
    print(check_hadamard(n, values))
