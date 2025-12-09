nombre_fichero = "libreria.py"

h_fichero = open(nombre_fichero,"r", encoding="utf-8")
for linea in h_fichero:
    if "def" in linea:
        print(linea, end="")