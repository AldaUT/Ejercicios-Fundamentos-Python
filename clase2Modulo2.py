#Clase Bucles o Loops: For/While

correct_guess = "manzana" 
guess_count = 0  
guess_limit = 3 #limite de intentos

while guess_count < guess_limit: 
    guess = input("Adivina la fruta: ").lower() # Admitir mayusculas y minusculas
    guess_count += 1 #1 input es igual a 1 intento
    if guess == correct_guess: #si se adivina en cada intento 1>3
        print("¡Felicidades, adivinaste la fruta!")
        break
    else: #si se acaba los intentos sin adivinar
        print("Ni modo, no adivinaste.") 