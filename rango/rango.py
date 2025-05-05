"""
Medidas de Dispersión
Rango=max(x)−min(x)
El rango es la diferencia entre el valor máximo y el mínimo.
Mide la extensión total del conjunto de datos.
"""
import matplotlib.pyplot as plt

cantidad = int(input("¿Cuántos números deseas ingresar? "))
datos = []
for i in range(cantidad):
    numero = float(input(f"Ingrese el número {i+1}: "))
    datos.append(numero)
    
maximo = max(datos) 
minimo = min(datos)
rango = maximo - minimo

plt.bar(range(len(datos)), datos, color='skyblue', label='Datos')
plt.axhline(minimo, color='green', linestyle='--', label=f'Mínimo: {minimo}')
plt.axhline(maximo, color='red', linestyle='--', label=f'Máximo: {maximo}')
plt.title(f"Gráfico de Barras - Rango = {rango}")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.legend()
plt.show()
