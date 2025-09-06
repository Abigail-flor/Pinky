#Ej.Continuar con confirmación

#Pregunta
while True:
    x = str(input("¿Desea continuar con el programa?"))
    if x.lower() != "si":
      break
print("Se ha acabado el programa")