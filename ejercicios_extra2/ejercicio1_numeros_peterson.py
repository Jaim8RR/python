#Ejercicio 1
#Pide al usuario un número de inicio y un número de fin. Muestra la lista de números que
#cumplan la condición de que sean números de Peterson entre ese número de inicio y ese
#número de fin.
#Repite esta acción mientras que el número de inicio sea menor que el número de fin.
#Números Peterson: Es un número que es igual a la suma de los factoriales de cada una de
#sus cifras, como por ejemplo el 145. 1! + 4! + 5! = 145"
inicio = 0
fin = 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def numero_peterson(numero):
    factoriales = list()
    numero_original = numero
    while numero != 0:
        #numero_factorial =factorial(numero %10) #me quedo la ultima cifra y le hago el factorial
        #factoriales.append(numero_factorial)
        factoriales.append(factorial(numero % 10))
        numero = numero//10
    return numero_original == sum(factoriales)

while inicio <= fin:

    try:
    
        inicio=int(input("Introduce un número de inicio:"))    
        fin=int(input("Introduce un número de fin:"))
        for i in range(inicio,fin+1):
            if numero_peterson(i):
                print(i,"es un numero de peterson")
            #else:
            #    print(i,"no es un numero de peterson")
    except Exception as e:
        print("No valido mete un numero",e)

print("adios")