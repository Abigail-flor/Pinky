#Mostrar la lista
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print("Lista original")
print(lista)
ultimo = lista[-1]
for i in range(11):
    lista.append(ultimo+i)
print("\nLista original modificada")
print(lista)