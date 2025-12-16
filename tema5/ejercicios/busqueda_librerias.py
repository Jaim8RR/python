#libreria = input("Introduce el nombre de tu libreria")
libreria = "libreria.py"
try:
    #h_fichero = open(nombre_fichero)
    with open(libreria) as h_fichero:
        for linea in h_fichero:
            if "def" in linea:
                nombre = linea[linea.find("def"):linea.find("(")]
                print("El nombre es",nombre.strip("def "))
                donde_se_abre = linea.find("(")
                donde_se_cierra = linea.find(")")
                parametros = linea[donde_se_abre+1:donde_se_cierra]
                if donde_se_abre != donde_se_cierra-1:
                    print("Los parametros son:",parametros)
                    numero_de_parametros = parametros.split(",")
                    print("El numero de parametros es:", len(numero_de_parametros))
                else: print("no hay parametros")
                
except Exception as e:
    print(e)