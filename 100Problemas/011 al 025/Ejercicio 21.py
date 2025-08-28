#Ej.Banquete por evento

#Ingresar los datos
evento = str(input("¿Cómo se llamará el evento? "))
fecha = str(input("¿Cuál sería la fecha? "))
asistentes = int(input("Ingresa la cantidad de personas que asistirán "))

#Operaciones
agua = 1.5*asistentes
carne = 350*asistentes
salsa = agua*0.25

#Mostrar resultados
print(f"El evento: {evento}, que se llevara a cabo el {fecha} con {asistentes} personas, ocupará:")
print(f"-{agua} litros de agua")
print(f"-{carne} gramos de carne")
print(f"-{salsa} litros de salsa")
