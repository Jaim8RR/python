nombre_fichero = "fichero.txt"
try:
    #h_fichero = open(nombre_fichero)
    with open(nombre_fichero) as h_fichero, open("texto.txt") as h_fichero:
        todo_el_fichero = h_fichero.read()
        print(f"la longitud del fichero es {len(todo_el_fichero)}")
        h_fichero.close()
except Exception as e:
    print("Error: ", e)