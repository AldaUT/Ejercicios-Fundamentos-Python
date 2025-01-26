# Se imprime la actividad
print ("Faltan 10 minutos para salir y me pidieron unas cosas para mañana ¿Qué debo hacer?:")
# se dan sugerencias de selección de la actividad con saltos de línea
Pregunta = input("A. Hacer la actividad y quedarme hasta tarde.\nB. Adelantar una parte y continuar el siguiente día.\nC. Dejarlo para el otro día y ver si no se me acumula mucha cosa.\n")
# seleccionar la respuseta y dar un mensaje
if Pregunta=="a" or Pregunta=="a." or Pregunta=="A." or Pregunta=="A":
    print("Espero no demorar tanto porque no me pagan las extras y luego no me pasa transporte")
elif Pregunta=="b" or Pregunta=="b." or Pregunta=="B." or Pregunta=="B":
    print("Haré mi mayor esfuerzo para no atrasarme en mis actividades.")
elif Pregunta=="c" or Pregunta=="c." or Pregunta=="C." or Pregunta=="C":
    print("Puedo sacar tiempo otro día o dejarlo para después.")
else:
    print("No está esa opción")  #kdjdjd