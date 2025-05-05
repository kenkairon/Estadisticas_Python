"""
La varianza mide cuánto se dispersan los valores respecto a la media.
Una varianza alta indica datos muy dispersos; una baja, datos más agrupados.
"""
cantidad = int(input("¿Cuántos números deseas ingresar? "))
datos = []
for i in range(cantidad):
    numero = float(input(f"Ingrese el número {i+1}: "))
    datos.append(numero)

media = sum(datos) / len(datos)
varianza = sum((x - media) ** 2 for x in datos) / len(datos)
print("Varianza:", varianza)
