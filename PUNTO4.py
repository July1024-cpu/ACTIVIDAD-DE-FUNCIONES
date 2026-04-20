# JULIANA GALVIS MONCADA CC. 1089379730

# 4. Escribe una función recursiva llamada invertir_cadena(texto) 
# que reciba un string y lo devuelva invertido.

def invertir_cadena(texto):
    if texto == "":          
        return ""
    else:
        return invertir_cadena(texto[1:]) + texto[0]

c= input("Escribe un texto: ")
print("Texto invertido:", invertir_cadena(c))
