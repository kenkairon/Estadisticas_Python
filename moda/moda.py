"""
3. Moda
La moda es el valor que más veces se repite en el conjunto de datos.
Puede haber más de una moda o ninguna.
"""
import matplotlib.pyplot as plt
import statistics

cantidad = int(input("¿Cuántos números deseas ingresar? "))
datos = []

# Ingresar los datos usando un for
for i in range(cantidad):
    numero = float(input(f"Ingrese el número {i+1}: "))
    datos.append(numero)
    
moda = statistics.mode(datos)
print("Moda:", moda)

# Crear el gráfico de barras con la línea de la moda
plt.bar(range(len(datos)), datos, color='skyblue', label='Datos')
plt.axhline(moda, color='red', linestyle='--', label=f'Moda: {moda}')
plt.title("Datos con Línea de la Moda")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.legend()
plt.show()

