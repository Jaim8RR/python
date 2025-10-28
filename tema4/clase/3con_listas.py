lista = [1, 2, 3, 4, "hola"]
print(len(lista))
#IN
for elemento in lista:
    print(elemento)
#RANGE
for i in range(0,len(lista)): #== for i in range(len(lista)):
    print(i,":",lista[i])

#Concatenar
lista_prueba = [5,6,7]
lista_prueba2 = ["UWU", "MIAU"]
todo = lista_prueba + lista_prueba2
print(todo,type(todo))
print(todo[3:50])

#Metodos
lista = list()
print(lista,type(lista))
lista.append("nuevo elemento")
lista.append(42)
lista.append(3.14, 100 , 99,2 , 3,4,5,6,7,8,9)
print(lista,"longitud:",len(lista))
lista.remove("nuevo elemento")
print(lista,"longitud:",len(lista))
lista.pop() #elimina el ultimo elemento
print(lista,"longitud:",len(lista))
lista.pop(0) #elimina el elemento en la posicion 0

#sort , modifica la lista original
numeros = [5,3,8,1,4]
print("Antes de sort:", numeros)
numeros.sort()
print("Despues de sort:", numeros)
#sorted , no modifica la lista original
numeros = [5,3,8,1,4]
print("Antes de sorted:", numeros)




