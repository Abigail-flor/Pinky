def creciente(lista): #Ordena de forma creciente
    return sorted(lista)
def decreciente(lista): #Ordena de forma decreciente
    return sorted(lista, reverse=True)
def eliminarPorI(lista, indice): #Eliminar pir índice (pop) y regresa el valor eliminado
    if 0<=indice < len(lista):
        return lista.pop(indice)
    else:
        return None
def eliminarPorD(lista, dato):
    if dato in lista:
        lista.remove(dato)
    return lista
def calcularEstad(lista):
    if len(lista) == 0:
        return None, None, None
    promedio = sum(lista)/len(lista)
    maxi = max(lista)
    mini = min(lista)
    return promedio, maxi, mini
numeros = [9, 4, 2, 7, 12, 3]
print("Lista real:", numeros)
print("Lista en orden creciente:", creciente(numeros))
print("Lista en orden decreciente:", decreciente(numeros))
valorElim = eliminarPorI(numeros, 3)
print("Valor que se elimina por el índice 3:", valorElim)
print("Lista después:", numeros)
numActual = eliminarPorD(numeros, 5)
print("Lista después de eliminar por dato 5:", numActual)
promedio, maxi, mini = calcularEstad(numActual)
print(f"Promedio: {promedio}, Máximo: {maxi}, Mínimo: {mini}")