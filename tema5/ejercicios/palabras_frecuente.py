#Programación en Python
#4.- Ejercicios
#4.1.- Ejercicio: Palabras más frecuentes en un texto
#A partir de los dos ficheros de texto que se adjuntan:
#galaxia.txt
#galaxy.txt
#Muestra, de cada fichero, las 10 palabras más utilizadas en el mismo, por orden de más
#frecuente a menos frecuente.
#Imprescindible:
#● Utiliza diccionarios para almacenar la frecuencia de las palabras
#● Utiliza una lista auxiliar de tuplas (valor,clave) para ordenar los resultados.
galaxia = "galaxia.txt"
galaxy = "galaxy.txt"
palabras = {}
words = {}
try:
    #h_fichero = open(nombre_fichero)
    with open(galaxia, encoding="utf-8") as fichero, open(galaxy, encoding="utf-8") as file:
        todo = fichero.read()
        todo = todo.lower()
        todo = todo.replace(",", "").replace(".", "").replace(";", "").replace(":", "").replace("¡", "").replace("!", "").replace("¿", "").replace("?", "").replace("\"", "").replace("(", "").replace(")", "").replace("?", " ").replace("%", " ").replace("[", " ").replace("]", " ")
        todo = todo.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
        todo = todo.split()

        whole = file.read()
        whole = whole.lower()
        whole = whole.replace(",", "").replace(".", "").replace(";", "").replace(":", "").replace("¡", "").replace("!", "").replace("¿", "").replace("?", "").replace("\"", "").replace("(", "").replace(")", "").replace("?", " ").replace("%", " ").replace("[", " ").replace("]", " ")
        whole = whole.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
        whole = whole.split()
    for word in whole:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    for palabra in todo:
        if palabra in palabras:
            palabras[palabra] += 1
        else:
            palabras[palabra] = 1
    # Mostrar las 10 palabras más frecuentes en cada fichero
    # galaxia.txt
    print("Las 10 palabras más frecuentes en galaxia.txt son:")
    lista_palabras = []
    for clave, valor in palabras.items():
        lista_palabras.append((valor, clave))
    lista_palabras.sort(reverse=True)
    for i in range(10):
        print(f"{i+1}.- {lista_palabras[i][1]} : {lista_palabras[i][0]} veces")
    # galaxy.txt
    print("\nLas 10 palabras más frecuentes en galaxy.txt son:")
    lista_words = []
    for key, value in words.items():
        lista_words.append((value, key))
    lista_words.sort(reverse=True)
    for j in range(10):
        print(f"{j+1}.- {lista_words[j][1]} : {lista_words[j][0]} times")

except Exception as e:
    print("Error: ", e)