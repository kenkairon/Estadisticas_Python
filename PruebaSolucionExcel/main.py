import pandas as pd
import matplotlib.pyplot as plt
import statistics
import numpy as np
from openpyxl import load_workbook
from openpyxl.drawing.image import Image as ExcelImage

# 1. Ingresar datos
cantidad = int(input("¿Cuántos números deseas ingresar? "))
datos = []
for i in range(cantidad):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    datos.append(numero)

# 2. Calcular estadísticas
media = statistics.mean(datos)
mediana = statistics.median(datos)
moda = statistics.mode(datos)
varianza = statistics.variance(datos) if len(datos) > 1 else 0
desviacion = statistics.stdev(datos) if len(datos) > 1 else 0

# 3. Crear DataFrames
df_datos = pd.DataFrame({'Valores': datos})
df_estadisticas = pd.DataFrame({
    'Estadística': ['Media', 'Mediana', 'Moda', 'Varianza', 'Desviación estándar'],
    'Resultado': [media, mediana, moda, varianza, desviacion]
})

# 4. Guardar los datos en un Excel
archivo_excel = 'estadisticas_completas.xlsx'
with pd.ExcelWriter(archivo_excel, engine='openpyxl') as writer:
    df_datos.to_excel(writer, sheet_name='Datos', index=False)
    df_estadisticas.to_excel(writer, sheet_name='Estadísticas', index=False)

# 5. Crear gráfico
plt.figure(figsize=(10, 6))
plt.plot(datos, marker='o', label='Datos', color='gray')
plt.axhline(media, color='red', linestyle='--', label=f'Media: {media:.2f}')
plt.axhline(mediana, color='green', linestyle='--', label=f'Mediana: {mediana:.2f}')
plt.axhline(moda, color='blue', linestyle='--', label=f'Moda: {moda:.2f}')
plt.title('Datos con Media, Mediana y Moda')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.tight_layout()
imagen = 'grafico_estadistico_completo.png'
plt.savefig(imagen)
plt.close()

# 6. Insertar gráfico en el Excel
wb = load_workbook(archivo_excel)
ws = wb['Estadísticas']
img = ExcelImage(imagen)
img.anchor = 'E2'  # Puedes cambiar la celda si quieres mover el gráfico
ws.add_image(img)
wb.save(archivo_excel)

print(f"✅ Archivo '{archivo_excel}' creado con estadísticas completas y gráfico insertado.")
