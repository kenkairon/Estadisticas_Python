cantidad = int(input("¿Cuántos números deseas ingresar? "))
datos = []
for i in range(cantidad):
    numero = float(input(f"Ingrese el número {i+1}: "))
    datos.append(numero)

import statistics
varianza = statistics.variance(datos)  # para muestra
# Para población completa:
import numpy as np
varianza_poblacional = np.var(datos)

print("Varianza (muestra):", varianza)
print("Varianza (población):", varianza_poblacional)

import matplotlib.pyplot as plt

media = sum(datos) / len(datos)
desviaciones = [x - media for x in datos]

plt.bar(range(len(datos)), datos, color='skyblue', label='Datos')
plt.axhline(media, color='red', linestyle='--', label=f'Media: {media:.2f}')

# Dibujar líneas desde cada barra hasta la media
for i, valor in enumerate(datos):
    plt.plot([i, i], [valor, media], color='gray', linestyle=':', linewidth=1)

plt.title("Visualización de la Varianza respecto a la Media")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.legend()
plt.show()
