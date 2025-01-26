import random # Modulo para aplicar una variación aleatoria 

# Día de la semana
Día = input("¿Qué día es hoy? (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado): ").capitalize()

# Determinamos el nivel de estrés y probabilidad de no hacer bien la tarea
if Día == "Lunes":
    nivel_estres = "Bajo"
    calidad_tarea = "Bien hecha"
elif Día == "Martes":
    nivel_estres = "Bajo"
    calidad_tarea = "Bien hecha"
elif Día == "Miércoles":
    nivel_estres = "Moderado"
    calidad_tarea = "Bien hecha"
elif Día == "Jueves":
    nivel_estres = "Alto"
    calidad_tarea = "Puede que no esté bien hecha"
elif Día == "Viernes":
    nivel_estres = "Muy alto"
    # Probabilidad random de que la tarea no quede bien hecha
    calidad_tarea = "Probabilidad alta de no quedar bien hecha" if random.random() < 0.7 else "Bien hecha, pero con estrés"
elif Día == "Sábado":
    nivel_estres = "Extremo"
    calidad_tarea = "Muy probablemente no quedará bien hecha"
else:
    #Control para valores no validos
    nivel_estres = "Desconocido" 
    calidad_tarea = "Desconocida"

# Resultado
print(f"Hoy es {Día}. Nivel de estrés: {nivel_estres}. La tarea está: {calidad_tarea}.") #