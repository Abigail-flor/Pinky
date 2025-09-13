#Listas de ahorradores y de sus ahorros
ahorradores = ["Jaime", "Alicia", "Laura", "Fabián", "Enrique", "Lucas"]
ahorros = [1256330, 989, 13452, 999, 1000, 1700201]
for i in range(len(ahorradores)):
    if ahorros[i]>1000000:
        print(f"Nombre: {ahorradores[i]}, Ahorros: {ahorros[i]} - Ya merito te retiras")
    elif ahorros[i]<1000: 
        print(f"Nombre: {ahorradores[i]}, Ahorros: {ahorros[i]} - No tendrás para tu futuro")
    else:
        print(f"Nombre: {ahorradores[i]}, Ahorros: {ahorros[i]}")