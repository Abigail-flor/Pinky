def correo():
    email = str(input("Por favor, ingrese un correo electrónico: "))
    if "@" in email:
        print("El correo electrónico es válido")
    else:
        print("El correo electrónico es inválido")
    return
correo()
