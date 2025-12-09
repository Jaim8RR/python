nombre = "ficheros2.txt"
lista = ["linea1","linea segunda","he terminado"]
try:
    with open(nombre,"w") as hfile:
        for linea in lista:
            hfile.write(linea +"\n")
except Exception as e:
    print("ERROR :",e)