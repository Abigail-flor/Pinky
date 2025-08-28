#Ej.Precio con IVA

#Recibir el producto y el precio
producto = str(input("Ingrese el nombre del producto, por favor "))
precio = float(input("¿Cuál es el precio? "))

#Calcular IVA
final = precio*1.16

#Mensaje
print(f"El producto {producto}, cuesta: ${precio} y su precio con IVA incluido es de: ${final}")