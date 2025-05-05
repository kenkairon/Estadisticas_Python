import matplotlib.pyplot as plt

datos = [10, 20, 30, 40]
media = sum(datos) / len(datos)
print("Media:", media)

plt.hist(datos, bins=5, color='lightgreen', edgecolor='black')
plt.axvline(media, color='red', linestyle='--', label=f'Media: {media:.2f}')
plt.title("Histograma con la Media")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.legend()
plt.show()
