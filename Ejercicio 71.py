import sympy as sp 

x = sp.symbols("x") 
ecuacion = sp.Eq(x**2 - 5*x + 7, 0) 
print("Sol. ",sp.solve(ecuacion, x)) 
ecn1= sp.Eq(7*x**2+9*x-7, 8*x**2-2*x-3) 
print("Sol. ", sp.solve(ecn1, x))