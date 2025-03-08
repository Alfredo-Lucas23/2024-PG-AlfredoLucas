import random

# Definimos las dimensiones de la matriz
ciudades = ["Cuenca", "Manta", "Ibarra"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Inicializamos la matriz 3D con temperaturas aleatorias
matriz_temperaturas = [[[random.uniform(15, 30) for _ in range(len(dias_semana))] for _ in range(semanas)] for _ in range(len(ciudades))]

# Calcular y mostrar el promedio de temperaturas para cada ciudad por semana
for i in range(len(ciudades)):
    print(f"Promedio de temperaturas para {ciudades[i]}:")
    for semana in range(semanas):
        suma_temperaturas = 0
        for dia in range(len(dias_semana)):
            suma_temperaturas += matriz_temperaturas[i][semana][dia]
        promedio = suma_temperaturas / len(dias_semana)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")