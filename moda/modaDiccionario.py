import matplotlib.pyplot as plt
from collections import Counter # Importar Counter para contar frecuencias

cantidad = int(input("¿Cuántos números deseas ingresar? "))
datos = []

# Ingresar los datos usando un for
for i in range(cantidad):
    numero = float(input(f"Ingrese el número {i+1}: "))
    datos.append(numero)
    

frecuencias = Counter(datos) # Contar frecuencias
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