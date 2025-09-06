#Ej.Confirmación de contraseña(sin límite)

c = str(input("Ingrese una contraseña: "))
d = str(input("Vuelve a ingresarla: "))
while c != d:
    c = str(input("Ingrese la contraseña: "))
    d = str(input("Vuelve a ingresarla: "))

print("Son correctas")