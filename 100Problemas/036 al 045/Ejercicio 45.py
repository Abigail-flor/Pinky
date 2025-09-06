#Ej.Calculadora con repetición por operación

print("***CALCULADORA***")
#Ciclo del programa completo
while True:
    print("\nOperaciones:")
    print("1.-Suma")
    print("2.-Resta")
    print("3.-Multiplicación")
    print("4.-División")
    print("5.-Exponente")
    print("6.-Módulo")
    #Ciclo para repetir las operaciones
    while True:
        opcion = int(input("Ingrese una opción del 1 al 6: "))
        numero= float(input("Ingrese el primer número: "))
        numero2= float(input("Ingrese el segundo numero: "))
        if opcion == 1:
            resultado= numero+numero2
            print(f"El resultadode la suma es: {resultado}")
        elif opcion == 2:
            resultado=numero-numero2
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == 3:
            resultado=numero*numero2
            print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == 4:
            if numero2 != 0:
                resultado=numero/numero2
                print(f"El resultado de la división es: {resultado}")
            else:
                print("Esta indefinida la división")
        elif opcion == 5:
            resultado= numero**numero2
            print(f"El resultado es: {resultado}")
        elif opcion ==6:
            if numero2 != 0:
                resultado = numero%numero2
                print(f"El resultado es: {resultado}")
            else:
                print("El módulo no se puede realizar con 0")
        else:
            print("Opción invalida")
            break
        repetir = input("¿Desea repetir la misma operación? (si o no): ")
        if repetir.lower() != "si":
            break
    otro = input("¿Desea realizar otra operación distinta? (si o no): ")
    if otro.lower() !="si":
        print("Programa finalizado")
        break