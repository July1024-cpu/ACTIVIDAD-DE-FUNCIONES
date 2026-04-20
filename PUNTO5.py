# JULIANA GALVIS MONCADA CC. 1089379730

# 5. Este ejercicio sustituye la lógica de un acumulador 
# (reduce) o la funciónmax(). Queremos encontrar el número 
# más grande comparando elementos uno a uno.

def m(lista):
    if len(lista) == 1:          
        return lista[0]
    else:
        mayor= m(lista[1:])
        if lista[0] > mayor:
            return lista[0]
        else:
            return mayor
        
n = input("Escribe números separados por espacios: ")
n = [int(x) for x in n.split()]
print(m(n))