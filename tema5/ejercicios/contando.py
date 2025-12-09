nombre_fichero = "contando.py"
h_fichero = open(nombre_fichero,"r", encoding="utf-8")
contador = 0
for linea in h_fichero:
    contador = contador +1
print("Mi programa tiene ",contador ,"lineas")