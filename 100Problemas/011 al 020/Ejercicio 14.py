#Ej.Series favoritas

#Ingresar las películas
series = str(input("Hola amigo!...¿Cuál es tu o tus series favoritas? (separa con comas) "))

#Si se necesita lista de las series
lista = [s.strip() for s in series.split(",")]

#Mensaje
print(f"Wow, suena interesante, espero poder ver algún día: ")

#Esablecer el bucle de la lista
for s in lista:
    print(f"-{s}")
