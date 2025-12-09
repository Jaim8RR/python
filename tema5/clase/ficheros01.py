nombre_fichero = "fichero.txt"

h_fichero = open(nombre_fichero,"r", encoding="utf-8")
for linea in h_fichero:
    print(linea, end="")
    if "DIO" in linea:
        print("Esta el dio loco")
    

