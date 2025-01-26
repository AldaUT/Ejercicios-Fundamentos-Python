def calcular_diferencia_años():
    print("Bienvenido al programa de cálculo de diferencia de años.")
    
    # Solicitar el año actual
    año_actual = int(input("Introduce el año actual: "))
    
    # Solicitar otro año para calcular
    año_ingresado = int(input("Introduce otro año para calcular: "))
    
    # Calcular la diferencia entre los años
    diferencia = año_actual - año_ingresado
    
    # Evaluar los diferentes casos
    if diferencia == 0:
        print("Has introducido el mismo año que el actual.")
    elif diferencia > 0:
        if diferencia == 1:
            print(f"Desde el año {año_ingresado} ha pasado 1 año.")
        else:
            print(f"Han pasado {diferencia} años desde el año que has introducido.")
    else:  # diferencia < 0
        diferencia = abs(diferencia)
        if diferencia == 1:
            print(f"Para llegar a {año_ingresado} hace falta 1 año.")
        else:
            print(f"Faltan {diferencia} años para llegar al año que has introducido.")

# Ejecutar el programa
calcular_diferencia_años() #