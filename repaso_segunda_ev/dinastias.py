#EJERCICIO1: Dinastías
    #En la monarquía española, cada rey se nombra por su nombre de pila y un número romano (Ejemplo,
    #Juan Carlos I), que indica cuántos reyes con ese nombre de pila ha habido, incluído él.
    #El rey te ha encargado un programa que, dado un fichero con los nombres de pila de los reyes,
    #pregunte nombres de los posibles sucesores e indique, con cada sucesor, el nombre completo que
    #tendría. Sigue pidiendo nombres hasta que digan adios.
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'dinastias.csv')
csv_file = os.path.join(os.path.dirname(file_path), 'dinastias.csv')
csv = open(csv_file,"r", encoding="utf8")
#separo cada nombre separado por comas
def base10_to_roman(number):
    # Mapping values to symbols in descending order
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    roman_numeral = ""
    i = 0
    
    
    while number > 0:
        # calculate how many times the current symbol fits
        count = number // values[i]
        roman_numeral += symbols[i] * count
        # Update the remaining number
        number %= values[i]
        i += 1
        
    return roman_numeral
    
dinasty = dict()    
for line in csv:
            name = ""
            
            for char in line:                    
                if char == ',':
                    if name in dinasty:
                        dinasty[name] += 1
                    else:
                        dinasty[name] = 1
                    name = ""                   
                else:
                    name += char

while True:
    successor = input("Introduce el nombre del sucesor (o 'adios' para salir): ")
    if successor.lower() == 'adios':
        print("Adiós!")
        break
    if successor in dinasty:
        number = dinasty[successor] + 1
    else:
        number = 1
    full_name = f"{successor} {base10_to_roman(number)} de españa"
    print(f"El nombre completo del sucesor sería: {full_name}")


