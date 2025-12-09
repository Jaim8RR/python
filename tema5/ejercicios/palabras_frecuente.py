galaxia = "galaxia.txt"
galaxy = "galaxy.txt"
palabras = {}
words = {}
try:
    #h_fichero = open(nombre_fichero)
    with open(galaxia) as fichero, open(galaxy) as file:
        todo = fichero.read()
        whole = file.read()
        todo = todo.split()
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

except Exception as e:
    print("Error: ", e)