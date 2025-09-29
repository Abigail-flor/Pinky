def numero():
    n = int(input("Ingrese un número: "))
    if n<=1:
        print("El número no es primo")
        return
    for i in range(2, n):
        if n % i == 0:
            print("El número no es primo")
            return
    print("El número es primo")
numero()