"""
La media es el valor promedio de un conjunto de datos, 
obtenido sumando todos los valores y dividiéndolos por la cantidad de elementos.
Indica el punto de equilibrio de los datos.
"""

import matplotlib.pyplot as plt

# Solicitar cuántos datos quiere ingresar
cantidad = int(input("¿Cuántos números deseas ingresar? "))
datos = []

# Ingresar los datos usando un for
for i in range(cantidad):
    numero = float(input(f"Ingrese el número {i+1}: "))
    datos.append(numero)

# Calcular la media
media = sum(datos) / len(datos)

# Crear el gráfico de barras con la línea de la media
plt.bar(range(len(datos)), datos, color='skyblue', label='Datos')
plt.axhline(media, color='red', linestyle='--', label=f'Media: {media:.2f}')
plt.title("Datos con Línea de la Media")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.legend()
plt.show()
