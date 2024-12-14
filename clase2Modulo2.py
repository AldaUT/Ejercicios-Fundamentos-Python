#Clase Bucles o Loops: For/While

correct_guess = "manzana" 
guess_count = 0  
guess_limit = 3

while guess_count < guess_limit:
    guess = input("Adivina la fruta: ").lower()
    guess_count += 1
    if guess == correct_guess:
        print("¡Felicidades, adivinaste la fruta!")
        break
    else:
        print("Ni modo, no adivinaste.")

if guess != correct_guess:
    print("¡Se acabaron los intentos! La respuesta correcta era:", correct_guess)