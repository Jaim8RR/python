#ordenando un diccionario por clave y valor usando tuplas
diccionario = {3: "tercero", 4: "cuarto", 1: "primero", 2: "segundo"}
print(diccionario)

#sort convirtiendo el diccionario en lista, se ordena por clave
lista = list(sorted(diccionario.items()))
lista2 = list(diccionario.items())
lista2.sort()
print(lista)
print(lista2)
#sort convirtiendo el diccionario en lista, se ordena por valor
lista3 = list()
for clave, valor in diccionario.items():
    lista3.append((valor, clave)) #tupla (valor, clave)
lista3.sort()
print(lista3)
diccionario_ordenado = dict()
for valor, clave in lista3:
    diccionario_ordenado[clave] = valor
print(diccionario_ordenado)
    