#Crear una lista rellenable
lista = []
opcion = str(input("¿Desea ingresar algún dato?: "))
while opcion.lower() == "si":
    x = input("Ingrese algún dato: ")
    lista.append(x)
    opcion = str(input("¿Desea ingresar algún dato?: "))
lista.sort()
print("\n****LISTA COMPLETA****")
for i in lista:
    print(i)
    