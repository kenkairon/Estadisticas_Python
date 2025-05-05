# mediaConLibrerias.py
import statistics
import matplotlib.pyplot as plt

# Solicitar cuántos datos quiere ingresar
cantidad = int(input("¿Cuántos números deseas ingresar? "))
datos = []

# Ingresar los datos usando un for
for i in range(cantidad):
    numero = float(input(f"Ingrese el número {i+1}: "))
    datos.append(numero)


media = statistics.mean(datos)
print("Media:", media)

# Crear el gráfico de Bloxplot con la línea de la media
plt.boxplot(datos, vert=False)
plt.axvline(media, color='red', linestyle='--', label=f'Media: {media:.2f}')
plt.title("Boxplot con la Media")
plt.legend()
plt.show()

