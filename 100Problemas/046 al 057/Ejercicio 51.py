#Registrar la lista de nombres y asistencia
nombres = []
asistencia = []
#Preguntar por la canyidad de trabajadores 
n = int(input("Ingrese la cantiad de trabajadores: "))
#Escribir un for para que de el tope de lista con n trabajadores
for i in range(n):
    nombre = str(input("Ingrese el nombre del trabajador: "))
    while True:
        asiste = int(input("¿Hoy se presento a laborar?: "))
        if asiste == 0:
            asiste = "faltó"
            break
        elif asiste == 1:
            asiste = "asistió"
            break
        print("Solo se admite 0 para falta y 1 de asistencia")
    asistencia.append(asiste)
    nombres.append(nombre)
#Imprime la lista de asistencia y el nombre
print("\n***Lista de asistencia***")
for i in range(n):
    print(f"{nombres[i]}, - , {asistencia[i]}")