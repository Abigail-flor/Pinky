print("¡Bienvenido a Llenando una lista de números!")
def miLista():
    n = int(input("\n¿De cuántas casillas quieres qeu sea tu lista?: "))
    laLista = [] #Empezamos la lista vacía despues de mencionar los casilleros
    for i in range(n):
        numeros = float(input("Por favor, ingrese un número: "))
        laLista.append(numeros)
    return laLista #Guardamos la información en la lista
print(miLista()) #Imprimimos la variable
