numero = int(input("dime un numero entero PARA CUENTA ATRAS8: "))
while numero >0:
    print(numero)
    numero = numero -1
print("Explosion")
# do while no existe
# de la forma pitonica con true break continue
while True:
    print("Estoy en bucle")
    salir = input("Quieres salir? s/n")
    if salir.lower()== "s":
        break
    else:
        continue

#de la forma tradicional
seguir = True
while seguir:
    print("Estoy en bucle2")
    salir = input("Quieres salir2? s/n")
    if salir.lower()== "s":
        seguir = False 
    


