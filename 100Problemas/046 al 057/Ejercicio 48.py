#Crear listas
nombre = ["lapices", "mochilas", "jugos", "libretas", "platos"]
clave = ["3106", "3172", "4453", "3190", "4471"]
piezas = [28, 15, 20, 52, 105]
#Preguntar por el indice que desea buscar
i = int(input("Ingrese el índice del producto que desea buscar (1-5): "))
if 1<=i<=5:
    print(f"\nNombre: {nombre[i-1]}\nCódigo: {clave[i-1]}\nPiezas: {piezas[i-1]}")
else:
    print("Índice incorrecto")
    