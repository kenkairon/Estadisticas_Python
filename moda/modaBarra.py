import matplotlib.pyplot as plt
from collections import Counter

datos = [12, 15, 14, 12, 13, 12, 18]

# Contar frecuencias
frecuencias = Counter(datos)
print("Frecuencias:", frecuencias)
# Crear gráfico
plt.bar(frecuencias.keys(), frecuencias.values(), color='lightgreen')
plt.title("Frecuencia de valores - Moda")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")

# Resaltar la moda
moda = max(frecuencias, key=frecuencias.get)
plt.axvline(moda, color='red', linestyle='--', label=f'Moda: {moda}')
plt.legend()
plt.show()
