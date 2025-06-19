notas = [
    [4.5, 3.8, 5.0],
    [4.0, 4.2, 4.5],
    [3.2, 3.5, 4.0]
]

prom_estudiantes = [sum(fila) / len(fila) for fila in notas]
prom_asignaturas = [sum(col) / len(notas) for col in zip(*notas)]
todos_aprobaron = all(all(nota >= 4.0 for nota in fila) for fila in notas)
alerta = [f"¡Alerta! Promedio del estudiante {i+1} es bajo: {prom:.2f}"
           for i, prom in enumerate(prom_estudiantes) if prom < 3.5]

print("Promedios por estudiante:")
for i, prom in enumerate(prom_estudiantes, start=1):
    print(f"Estudiante {i}: {prom:.2f}")

print("Promedios por asignatura:")
for i, prom in enumerate(prom_asignaturas, start=1):
    print(f"Asignatura {i}: {prom:.2f}")

print("¿Todos aprobaron?")
print("Sí" if todos_aprobaron else "No")

if alertas:
    print("Alertas:")
    for alerta in alertas:
        print(alerta)
