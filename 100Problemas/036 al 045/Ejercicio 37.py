#Ej.Interés compuesto con repetición

C = float(input("Ingrese el Capital inicial: "))
i = float(input("Ingrese la tasa de interés: "))
n = int(input("Ingrese el número de periodos: "))
M = C*(1+i)**n
print(f"El monto final es: {M}")
j = str(input("¿Desea realizar otro cálculo de interés compuesto?: "))
while j == "si" or j == "Si":
    C = float(input("Ingrese el Capital inicial: "))
    i = float(input("Ingrese la tasa de interés: "))
    n = int(input("Ingrese el número de periodos: "))
    M = C*(1+i)**n
    print(f"El monto final es: {M}")
    j = str(input("¿Desea realizar otro cálculo de interés compuesto?: "))
    while j == "no" or j == "No":
        print("Usted ha terminado el cálculo")
        break