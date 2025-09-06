#Ej.Validación de número entre 1 y 5

while True:   #Detectar el veridico la condición
    numero = int(input("Ingrese un  número dentro del rango de 1 al 5: "))
    if numero>=1 and numero<=5: #Condicionar el rango
        print("¡Muy bien!, has ingresado un número dentro del rango")
        break #romper la condición mientras, cuando fue correcta la respuesta del usuario
    else:  #Si fue incorrecto
        print("Por favor, debe ser un número del rango. Intentelo de nuevo")