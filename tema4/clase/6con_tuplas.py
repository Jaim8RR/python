#ordenando un diccionario por clave y valor usando tuplas
diccionario = {3: "tercero", 4: "cuarto", 1: "primero", 2: "segundo"}
print(diccionario)

#sort convirtiendo el diccionario en lista
lista = list(sorted(diccionario.items()))
lista2 = list(diccionario.items())
lista2.sort()
print(lista)
print(lista2)