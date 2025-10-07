def suma_anteriores_bucle(numero):
    total = 0
    while numero > 0:
        total = total + numero
        numero = numero -1
    return total

def suma_anteriores_recursividad(numero,total=0):
    if numero == 0:
        return total
    else:
        total = total + numero
        numero = numero -1
        return suma_anteriores_recursividad(numero,total)


print(suma_anteriores_bucle(4))#4+3+2+1
print(suma_anteriores_recursividad(4))#4+3+2+1

    
    
        