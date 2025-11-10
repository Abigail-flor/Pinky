import re

contraseña = input("Ingresa una contraseña: ")

if (len(contraseña) >= 8 and
    re.search(r'[A-Z]', contraseña) and
    re.search(r'[a-z]', contraseña) and
    re.search(r'\d', contraseña)):
    print("Contraseña segura")
else:
    print("Insegura")
