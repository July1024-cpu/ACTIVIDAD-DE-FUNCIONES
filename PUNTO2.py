# JULIANA GALVIS MONCADA CC. 1089379730

# 2. En lugar de usar filter y map, crearemos una función que recorra
#una lista, decida si un número es par y, si lo es, lo eleve al cuadrado,
#todo en un solo paso recursivo.

def pares(lista):
    if lista == []:         
        return []
    if lista[0] % 2 == 0:    
        return [lista[0]**2] + pares(lista[1:])
    else:                    
        return pares(lista[1:])
    
n= input("Escribe números separados por espacios: ")
n = [int(x) for x in n.split()]
print(pares(n))
