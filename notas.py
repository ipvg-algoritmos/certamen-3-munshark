notas = [
    [4.5, 3.8, 4.2],
    [3.2, 3.0, 2.8],
    [4.0, 4.1, 3.9]
]

promedios_estudiantes = [sum(fila)/len(fila) for fila in notas]
promedios_asignaturas = [sum(col)/len(col) for col in zip(*notas)]
todos_aprobaron = all(nota >= 4.0 for fila in notas for nota in fila)
bajo_rendimiento = [i+1 for i, prom in enumerate(promedios_estudiantes) if prom < 3.5]

print("Promedios por estudiante:")
for i, prom in enumerate(promedios_estudiantes, 1):
    print("Estudiante {i}: {prom:.2f}")

print("Promedios por asignatura:")
for i, prom in enumerate(promedios_asignaturas, 1):
    print("Asignatura {i}: {prom:.2f}")

print("¿Todos los estudiantes aprobaron todas las asignaturas?")
print(" Sí" if todos_aprobaron else " No")

if bajo_rendimiento:
    print(" Alerta: Los siguientes estudiantes tienen bajo rendimiento (promedio < 3.5):")
    for est in bajo_rendimiento:
        print(" - Estudiante {est}")
else:
    print(" Todos los estudiantes tienen buen rendimiento (promedio >= 3.5).")
