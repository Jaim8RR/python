#Ejercicio1: EJERCICIO DE LISTAS
#Considera una lista (lista = []). Puedes realizar los siguientes comandos:
#1. insert posicion entero: Inserta el entero en la posición de la lista. Si ya existe otro
#elemento en esa posición, lo inserta y desplaza el resto de elementos a la derecha
#2. print: Imprime la lista
#3. remove entero: Elimina la primera ocurrencia del entero
#4. append entero: Inserta el entero al final de la lista
#5. sort: Ordena la lista
#6. pop: Elimina el último elemento de la lista
#7. reverse: Invierte la lista


while comando == "fin":

    try:
    
        comando=int(input("Introduce un Comando"))
        if comando != "fin":
            if comando == "insert":
                print("inserta el entero en la posición de la lista, 0 3")

        
    except Exception as e:
        print(e)

print("adios")