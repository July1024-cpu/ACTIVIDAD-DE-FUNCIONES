# JULIANA GALVIS MONCADA CC. 1089379730

#1. Escribe una función llamada factorial(n) que calcule elproducto 
#de todos los números enteros positivos desde 1 hasta n.

def factorial(n):
    r= 1
    for i in range(1, n+1):
        r *= i
    return r

n = int(input("Ingresa un número entero positivo: "))
print("El factorial de", n, "es", factorial(n))
