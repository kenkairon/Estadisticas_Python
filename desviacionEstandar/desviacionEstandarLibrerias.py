import statistics

while True:
    try:
        cantidad = int(input("¿Cuántos números deseas ingresar? "))
        if cantidad < 2:
            print("⚠️ Debes ingresar al menos 2 números para calcular la desviación estándar.")
            continue

        datos = []
        for i in range(cantidad):
            numero = float(input(f"Ingrese el número {i+1}: "))
            datos.append(numero)

        desviacion_muestra = statistics.stdev(datos)  # muestra
        desviacion_poblacion = statistics.pstdev(datos)  # población

        print("✅ Desviación estándar (muestra):", desviacion_muestra)
        print("✅ Desviación estándar (población):", desviacion_poblacion)
        break  # salir del bucle si todo salió bien

    except ValueError:
        print("❌ Error: Ingresa solo números válidos.")
    except statistics.StatisticsError as e:
        print("❌ Error al calcular desviación estándar:", e)

    
