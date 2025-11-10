import re

texto = input("Ingresa un texto con fechas (dd/mm/aaaa): ")
fechas = re.findall(r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b', texto)
fechas = ["/".join(f) for f in fechas]
print("Fechas encontradas:", fechas)
