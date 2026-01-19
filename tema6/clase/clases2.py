string = str()
metodos = dir(string)
metodos_no_magicos = list()
for metodo in metodos:
    if "__" not in metodo :
        metodos_no_magicos.append(metodo)
for metodo in metodos_no_magicos:
    print("- ",metodo)

