#Ej.Confirmación de contraseña(con límite)

intentos = 3
for i in range (intentos):
    a = str(input("Ingrese una contraseña: "))
    b = str(input("Vuelve a ingresarla: "))
    if a == b:
        print("Son correctas")