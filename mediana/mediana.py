"""
La mediana es el valor que se encuentra en el centro del conjunto de datos ordenados. 
Si hay un número par de datos, se toma el promedio de los dos valores centrales.
Representa el valor medio, útil cuando hay datos extremos.
"""
import matplotlib.pyplot as plt
# Solicitar cuántos datos quiere ingresar
cantidad = int(input("¿Cuántos números deseas ingresar? "))
datos = []

# Ingresar los datos usando un for
for i in range(cantidad):
    numero = float(input(f"Ingrese el número {i+1}: "))
    datos.append(numero)

datos_ordenados = sorted(datos)
n = len(datos_ordenados)
if n % 2 == 0:
    mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
else:
    mediana = datos_ordenados[n//2]
print("Mediana:", mediana)


plt.boxplot(datos, vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title("Boxplot - Representación de la Mediana")
plt.xlabel("Valor")
plt.show()