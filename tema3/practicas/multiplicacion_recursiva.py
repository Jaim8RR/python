#La multiplcacion es la suma de n veces una cifra por la otra 3x5 es 3+3+3+3+3 o 5+5+5 esto es lo que debemos imprimir el desglose


# con bucle
def multiplacion_desglose_bucle(x,y):
    cadenaxvecesy = ""
    cadenayvecesx = ""
    for i in range(y):
        cadenaxvecesy += str(x)
        if i < y-1:
            cadenaxvecesy += " + "
    for j in range(x):
        cadenayvecesx += str(y)
        if j < x-1:
            cadenayvecesx += " + "
    return f"{x}x{y} = {cadenaxvecesy} = {cadenayvecesx}"


# con recursividad
def multiplicacion_desglose_recursiva_y(x, y):
    if y == 1:
        return str(x)
    else:
        return str(x) + " + " + multiplicacion_desglose_recursiva_y(x, y-1)

def multiplicacion_desglose_recursiva_x(x, y):
    if x == 1:
        return str(y)
    else:
        return str(y) + " + " + multiplicacion_desglose_recursiva_x(x-1, y)

    

entrada1 = int(input("Dime un numero: "))
entrada2 = int(input("Dime otro numero: "))
print("Con bucle: "+multiplacion_desglose_bucle(entrada1,entrada2))
print(f"Con recursividad: {entrada1}x{entrada2} = {multiplicacion_desglose_recursiva_y(entrada1,entrada2)} = {multiplicacion_desglose_recursiva_x(entrada1,entrada2)}")


