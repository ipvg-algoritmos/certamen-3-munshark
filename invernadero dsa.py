temperaturas = []

for i in range(5):
    temp = float(input(f"Ingrese la temperatura {i+1}: "))
    temperaturas.append(temp)

promedio = sum(temperaturas) / len(temperaturas)
maxima = max(temperaturas)
todas_entre_15_30 = all(15 <= t <= 30 for t in temperaturas)
advertencia_fuera_de_rango = any(t < 10 or t > 35 for t in temperaturas)

print("Temperaturas ingresadas: {temperaturas}")
print("Promedio: {promedio:.2f}°C")
print("Temperatura máxima: {maxima}°C")

if todas_entre_15_30:
    print("Todas las temperaturas están entre 15°C y 30°C.")
else:
    print("No todas las temperaturas están entre 15°C y 30°C.")

if advertencia_fuera_de_rango:
    print("Advertencia: Hay temperaturas fuera del rango permitido (10°C–35°C).")
