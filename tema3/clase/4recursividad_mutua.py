def es_par(numero):
    if numero == 0:
        return True
    else:
        return es_impar(numero - 1)

def es_impar(numero):
    if numero == 0:
        return False
    else:
        return es_par(numero - 1)

entrada = int(input("Dime un numero: "))
if es_par(entrada):
    print(f"El numero {entrada} es par")
else:
    print(f"El numero {entrada} es impar")