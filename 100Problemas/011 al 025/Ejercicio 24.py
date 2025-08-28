#Ej.Interés simple y compuesto

capital = float(input("Ingrese la capital inicial: "))
tasa = float(input("Ingrese el porcentaje de interes anual en decimal: "))
periodos = int(input("Ingrese el número de periodos anuales: "))

capfs = capital*(1+(tasa*periodos))
capfc = capital*((1+tasa)**periodos)

print(f"La capital final simple es de: {capfs}")
print(f"La capital final compuesta es de: {capfc}")
