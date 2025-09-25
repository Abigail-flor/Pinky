print("¡Bienvenido al transformador de números!")
numero = int(input("\nPor favor, ingrese un número dentro de un rango de (1 - 3999): "))
if numero<1 or numero>3999:
    print("Error: número fuera del rango (1...3999)")
else:
   #Tablas para el número
   millar = ["", "M", "MM", "MMM"]
   centena = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
   decena = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
   unidad = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
   #Para deshacer el número
   
   m = numero//1000
   c = (numero % 1000)//100
   d = (numero % 100)//10
   u = numero % 10
   romano = millar[m] + centena[c] + decena[d] + unidad[u]
   print(f"El número romano es: {romano}")