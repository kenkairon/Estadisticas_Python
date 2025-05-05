"""
Q1 (percentil 25): valor debajo del cual se encuentra el 25% de los datos.

Q3 (percentil 75): valor debajo del cual se encuentra el 75% de los datos.
"""
import numpy as np
import matplotlib.pyplot as plt

cantidad = int(input("¿Cuántos números deseas ingresar? "))
datos = []
for i in range(cantidad):
    numero = float(input(f"Ingrese el número {i+1}: "))
    datos.append(numero)

q1 = np.percentile(datos, 25)
q3 = np.percentile(datos, 75)
iqr = q3 - q1

print(f"Q1 (25%): {q1}")
print(f"Q3 (75%): {q3}")
print(f"Rango Intercuartílico (IQR): {iqr}")


