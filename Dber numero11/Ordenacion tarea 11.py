# Definir la matriz 3x3
matriz = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

# Función para ordenar una fila específica usando Bubble Sort
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]
    return matriz

# Fila a ordenar (por ejemplo, la primera fila)
fila_a_ordenar = 0
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

print("Matriz original:")
for fila in matriz:
    print(fila)

print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)