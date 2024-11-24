# Proyecto calculadora IMC
import time 

print("""
     \ O /        \ O /
      \|/   IMC    \|/ 
       |  Monitor   |
      / \          / \ 
""")
#Input para el Nombre
nombre = input("Introduzca por favor su nombre: ")
while not nombre.strip() or not all(c.isalpha() or c.isspace() for c in nombre):
    if not nombre.strip(): print("El nombre no puede estar vacío. Por favor ingréselo.")
    else: print("Error: El nombre no puede contener números ni caracteres especiales.")
    nombre = input("Introduzca por favor su nombre: ")
    nombre = nombre.strip().title() # Capitalizar el nombre

#Input para el Apellido Paterno
apellidoPaterno = input("Su apellido paterno: ")
while not apellidoPaterno.strip() or not apellidoPaterno.isalpha(): # Verificar que no esté vacío y que no contenga números o caracteres especiales
    if not apellidoPaterno.strip(): print("El apellido no puede estar vacío Por favor ingréselo.")
    else: print("Error: El apellido no puede contener números ni caracteres especiales.")
    apellidoPaterno = input("Introduzca por favor su apellido paterno: ")
    apellidoPaterno = apellidoPaterno.strip().capitalize() # Capitalizar el apellido 

#Input para el Apellido Materno
apellidoMaterno = input("Su apellido Materno: ")
while not apellidoMaterno.strip() or not apellidoMaterno.isalpha(): # Verificar que no esté vacío y que no contenga números o caracteres especiales
    if not apellidoMaterno.strip(): print("El apellido no puede estar vacío Por favor ingréselo.")
    else: print("Error: El apellido no puede contener números ni caracteres especiales.")
    apellidoMaterno = input("Introduzca por favor su apellido paterno: ")
    apellidoMaterno = apellidoMaterno.strip().capitalize() # Capitalizar el apellido 

print(f"Hola! {nombre} {apellidoPaterno} {apellidoMaterno}")
time.sleep(3)
print("Vamos a calcular tu Indice de masa corporal")

edad = int(input("Su edad: "))
while True:
    edad = input("Su edad: ").strip()  # Elimina espacios en blanco al principio y al final
    if edad.isdigit():  # Verifica si la entrada son solo números
        edad = int(edad)  # Convierte a entero
        if edad >= 18:
            break  # Sale del bucle si la edad es válida
        else: print("Error: Debe ser mayor o igual a 18 años.")
    else: print("Error: Debe ingresar un número entero válido.")

estatura = float(input("Su altura: "))
while not estatura or float(estatura) == 0:
    print("Error: La estatura no puede ser vacía o 0.")
    estatura = input("Introduzca por favor su altura (en metros): ")
estatura = float(estatura) #validación   

peso = float(input("Su peso en Kg: "))
peso = input("Su peso en Kg: ")
while not peso or float(peso) == 0:
    print("Error: El peso no puede ser vacío o 0.")
    peso = input("Introduzca por favor su peso en Kg: ")
peso = float(peso) #validación
