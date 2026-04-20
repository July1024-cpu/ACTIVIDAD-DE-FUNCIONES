# JULIANA GALVIS MONCADA CC. 1089379730

#3. Crea una función llamada suma_recursiva(lista) que reciba una lista de
#números y devuelva la suma total de sus elementos.


def suma_recursiva(lista):
    if lista == []:          # caso base: lista vacía
        return 0
    else:
        return lista[0] + suma_recursiva(lista[1:])

n = input("Escribe números separados por espacios: ")
n = [int(x) for x in n.split()]
print(suma_recursiva(n))
