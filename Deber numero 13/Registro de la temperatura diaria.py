import random

# Definimos las dimensiones de la matriz
ciudades = ["Ambato", "Esmeraldas", "Riobamba"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Inicializamos la matriz 3D con temperaturas aleatorias
# La matriz tiene dimensiones [ciudades][semanas][dias_semana]
matriz_temperaturas = [[[random.uniform(15, 30) for _ in range(len(dias_semana))] for _ in range(semanas)] for _ in
                       range(len(ciudades))]


def calcular_promedio_temperaturas(matriz_temperaturas, ciudades, dias_semana, semanas):
    """
    Calcula y muestra el promedio de temperaturas para cada ciudad por semana.

    Parámetros:
    matriz_temperaturas (list): Matriz 3D con las temperaturas.
    ciudades (list): Lista de nombres de ciudades.
    dias_semana (list): Lista de días de la semana.
    semanas (int): Número de semanas.
    """
    # Iteramos sobre cada ciudad
    for i in range(len(ciudades)):
        print(f"Promedio de temperaturas para {ciudades[i]}:")
        # Iteramos sobre cada semana
        for semana in range(semanas):
            suma_temperaturas = 0
            # Sumamos las temperaturas de cada día de la semana
            for dia in range(len(dias_semana)):
                suma_temperaturas += matriz_temperaturas[i][semana][dia]
            # Calculamos el promedio dividiendo la suma entre el número de días de la semana
            promedio = suma_temperaturas / len(dias_semana)
            print(f"  Semana {semana + 1}: {promedio:.2f}°C")


# Llamar a la función para calcular y mostrar los promedios
calcular_promedio_temperaturas(matriz_temperaturas, ciudades, dias_semana, semanas)