#Ej.Calificación de exámen

#Ingresa los datos
examen = int(input("Ingrese la cantidad de preguntas del exámen: "))
correctos = int(input("Ingrese las preguntas que obtuvo correctas: "))

#Cálculo
calif = (correctos*10)/examen

#Resultados
print(f"Su calificación final es de: {calif}")