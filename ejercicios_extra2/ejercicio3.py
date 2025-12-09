#hola me llamo (jaime) y estoy aprendiendo python {lol} #balanceada
#hola me llamo (jaime) y estoy aprendiendo python {lol}{ #no balanceada
#hola me llamo  y estoy a [prendiendo pyth] on {l(ol} (jaime) #no balanceada
#hola me [llamo (ja]ime) y estoy aprendiendo python {lol} #no balanceada
#Ejercicio 3
#Se entiende que una secuencia de caracteres está correctamente equilibrada con respecto a los paréntesis si cada uno de los paréntesis de apertura tiene su paréntesis cerrado. Cuando añadimos otros mecanismos de agrupación (como los corchetes, [ y ] o las llaves, { y }), el equilibrio se da si el número de aperturas de cada símbolo coincide con el de cierres y además se cierran en el orden correcto.
#Pide al usuario una cadena de caracteres y muestra por pantalla si esa cadena de caracteres está correctamente balanceada.
#Repite esta acción hasta que la cadena de caracteres sea igual a FIN
def cadena_equilibrada(texto):
    pila = []
    pares = {
        ")": "(",
        "}": "{",
        "]": "["
        }

    for caracter in texto:
        if caracter in "({[":
            pila.append(caracter)
        elif caracter in ")}]":
            if not pila or pila[-1] != pares[caracter]:
                return False
            pila.pop()
            

    return len(pila) == 0


texto = ""

while texto != "FIN":
    texto = input("Introduce una cadena de texto/FIN: ")
    if texto != "FIN":
        print("La cadena está balanceada" if cadena_equilibrada(texto) else "La cadena NO está balanceada")

