#Ej.Saludo con año de nacimiento

#Ingresa datos y responde 
nombre = str(input("Por favor, ingresa tu nombre "))
edad = int(input("Ingrese su edad y adivinare su año de nacimiento "))

año = 2025-edad
print(f"Mucho gusto {nombre}!, creo que naciste en el año: {año}")