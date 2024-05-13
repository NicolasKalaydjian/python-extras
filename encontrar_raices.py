import math

"""
Encuentra las raíces de la función en el intervalo [start, end]

Parametros:
- func: La función para la cual se busca las raices.
- start, end: Los extremos del intervalo [start, end] donde se buscará las raices.
El intervalo debe pertenecer al dominio de la función.

Retorna:
- roots: Lista con las raíces.
"""

def find_roots(func, start, end):
    precision = 2
    step = 10**(-precision-1)
    current_x = start
    current_value = func(current_x)
    roots = []

    while current_x <= end:
        current_x += step
        new_value = func(current_x)
        
        if current_value * new_value <= 0:
            root = round(current_x, precision)
            roots.append(root)
            
        current_value = new_value
        
        return roots

#Ejemplos

f1 = lambda x: (x+1)*(x-1)*(x-2) # Dom: R == (-1000,1000) // resultado: [-1, 1, 2]
f2 = lambda x: (x+1)*(x-1)*(x-math.sqrt(2)) # Dom: R == (-1000,1000) // resultado: [-1, 1, 1.41]
f3 = lambda x: x**3 + 2*x**2 - 1 # Dom: R == (-1000,1000) // resultado: [-1.62, -1, 0.62]
f4 = lambda x: 2*x+1 - 3/2 * (math.sqrt(1/x)) ** (4*x-1) # Dom: (0,+inf) == (0.01,1000) // resultado: [0.25, 0.58]
f5 = lambda x: math.sqrt(x) # Dom: [0,+inf) == (0,1000) // resultado: [0]
f6 = lambda x: math.log(x) # Dom: (0,+inf) == (0.01,1000) // resultado: [1]
f7 = lambda x: 1/x # Dom: R - {0} == (-1000,-0.01) + (0.01,1000) // resultado: []

roots_f1 = find_roots(f1, -1000, 1000)
roots_f2 = find_roots(f2, -1000, 1000)
roots_f3 = find_roots(f3, -1000, 1000)
roots_f4 = find_roots(f4, 0.01, 1000)
roots_f5 = find_roots(f5, 0, 1000)
roots_f6 = find_roots(f6, 0.01, 1000)
roots_f7 = find_roots(f7, -1000, -0.01) + find_roots(f7, 0.01, 1000)

roots_finded = [roots_f1, roots_f2, roots_f3, roots_f4, roots_f5, roots_f6, roots_f7]

#para quitar los ceros a las raices enteras
#roots_finded = [int(root) if root.is_integer() else root for root in roots_finded]

for i, roots in enumerate(roots_finded):
    roots = [int(root) if root.is_integer() else root for root in roots]
    print(f"Raices de la función {i+1}:")
    print(roots)