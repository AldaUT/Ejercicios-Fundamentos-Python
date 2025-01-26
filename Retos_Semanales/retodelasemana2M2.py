lista = []
print("Bienvenido al programa de registro de alumnos!")
cantidad = int(input("¿Cuántos alumnos quieres registrar? "))

for _ in range(cantidad):
    # Solicita el nombre del alumno y lo capitaliza.
    nombre = input("Escribe el nombre del alumno: ").capitalize()

    while True:
        # Pide al usuario cuántas calificaciones desea registrar (1 a 3).
        num_calificaciones = int(input(f"¿Cuántas calificaciones vas a registrar para {nombre}? (Elige entre 1 y 3): "))
        if 1 <= num_calificaciones <= 3:
            break
        else:
            print("Por favor, elige un número válido entre 1 y 3.")

    calificaciones = []
    for i in range(num_calificaciones):
        # Captura cada calificación del alumno y la guarda en la lista de calificaciones.
        calificacion = float(input(f"Escribe la calificación {i + 1} de {nombre}: "))
        calificaciones.append(calificacion)

    # Calcula el promedio de las calificaciones.
    promedio = sum(calificaciones) / len(calificaciones)
    lista.append([nombre, calificaciones, promedio])

# Muestra la lista de alumnos con sus calificaciones y promedios.
print("\nAquí está la lista de alumnos con sus promedios:")
for alumno in lista:
    nombre, calificaciones, promedio = alumno
    print(f"{nombre}: Calificaciones: {calificaciones}, Promedio: {promedio:.2f}") #
