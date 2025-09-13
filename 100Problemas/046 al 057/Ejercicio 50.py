#Crear las listas
nombre = ["lapices", "mochilas", "jugos", "libretas", "platos"]
clave = ["3106", "3172", "4453", "3190", "4471"]
piezas = [28, 15, 20, 52, 105]

#Crear Diccionario
productos = {}
for i in range(len(nombre)):
    productos [i+1] = {
       "nombre": nombre[i],
       "clave" : clave[i],
       "piezas": piezas[i]
    }
#Pedir opciones
print("Opciones:\n1.-Buscar por índice\n2.-Buscar por nombre\n3.-Buscar por clave\n4.-Mostrar diccionario completo\n5.-Salir")
op = int(input("Elija una opción: "))
if op == 1:
    i = int(input("Ingrese el índice del producto que desea buscar (1-5): "))
    if 1<=i<=5:
        print(f"\nNombre: {nombre[i-1]}\nCódigo: {clave[i-1]}\nPiezas: {piezas[i-1]}")
    else:
        print("Opción inválida")
elif op == 2:
    print(nombre)
    nom = str(input("Ingrese el nombre del producto: "))
    encontrado = False
    for datos in productos.values():
        if datos["nombre"].lower() == nom:
            print(f"\nNombre: {datos['nombre']}\nCódigo: {datos['clave']}\nPiezas: {datos['piezas']}")
            encontrado = True
            break
    if not encontrado:
        print("No esta ese producto, lea bien")
elif op == 3:
    print(clave)
    codigo = input("Ingrese el código: ")
    encontrado = False
    for datos in productos.values():
        if datos["clave"] == codigo:
            print(f"\nNombre: {datos['nombre']}\nCódigo: {datos['clave']}\nPiezas: {datos['piezas']}")
            encontrado = True
            break
    if datos["clave"] != codigo:
        print("Ese código no esta, chequese bien")
elif op == 4:
    print("\nDiccionario de productos:")
    print(productos)
elif op == 5:
    print("Ha terminado su busqueda")
else:
    print("No esta esa opción, lea bien")   