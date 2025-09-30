seguir = True
while seguir:
    nota = int(input("Dime un numrto entre el 1 y 10 "))
    if nota > 0 and nota < 11:
        seguir = False 
    else: print("numero fuera de rango")

print("tu numero es :",nota)