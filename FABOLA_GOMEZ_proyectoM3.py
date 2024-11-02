import random
import matplotlib.pyplot as plt

# Función para simular la caída de las canicas y calcular el contenedor final de cada una
def simular_canicas(num_canicas, num_niveles):
    """
    Simula la caída de canicas a través de una máquina de Galton.
    Cada canica tiene una probabilidad igual de moverse a la izquierda o a la derecha.
    
    Parámetros:
    - num_canicas: Número total de canicas que se lanzarán en la simulación.
    - num_niveles: Número de niveles con obstáculos en la máquina.
    
    Retorna:
    - contenedores: Una lista que contiene el conteo de canicas en cada contenedor final.
    """
    contenedores = [0] * (num_niveles + 1)  # Inicializar los contenedores
    for _ in range(num_canicas):
        posicion = 0  # Las canicas comienzan en la parte superior
        for _ in range(num_niveles):
            # Decidir aleatoriamente si va a la izquierda (0) o a la derecha (1)
            posicion += random.choice([0, 1])
        contenedores[posicion] += 1  # Incrementar el contenedor donde cae la canica
    return contenedores

# Función para graficar el histograma con los resultados de la simulación
def graficar_histograma(contenedores):
    """
    Grafica un histograma para visualizar la distribución de canicas en los contenedores.
    
    Parámetros:
    - contenedores: Lista con el conteo de canicas en cada contenedor.
    """
    plt.bar(range(len(contenedores)), contenedores, color='blue')
    plt.title('Simulación de la Máquina de Galton')  # Título del gráfico
    plt.xlabel('Número de Contenedor')  # Nombre del eje X
    plt.ylabel('Cantidad de Canicas')  # Nombre del eje Y
    plt.show()

# Parámetros para la simulación
num_canicas = 3000  # Cantidad de canicas
num_niveles = 12  # Número de niveles de obstáculos

# Simular la caída de las canicas
resultados_contenedores = simular_canicas(num_canicas, num_niveles)

# Graficar el histograma con los resultados
graficar_histograma(resultados_contenedores)