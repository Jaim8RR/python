#Ejercicio 2
#Pide al usuario un número entero positivo y muestra el número de cifras que tiene.
#Utiliza un algoritmo matemático, sin usar el número como cadena de caracteres u otra estructura o tipo de datos diferente al de número entero.
#Repite esta acción hasta que el usuario introduzca el número cero.
#Finalmente muestra el número con mayor número de cifras de los introducidos por el usuario y su número de cifras.
numero="hola"
numeros = list()
def cuenta_cifras(numeros):
    numero_cifras_max = ""
    cifras_max =0

    for numero in numeros:
        
        numero_original = numero
        cifras = 0

        while numero!=0:
            numero = numero//10
            cifras= cifras+1
            if cifras > cifras_max:
                #print("remplazo", numero_cifras_max, "con ",numero)#estaba borrando el numero original igual que en el anterior lol
                numero_cifras_max = numero_original
                cifras_max = cifras
        print(numero_original, "tiene ", cifras," cifras")
    print("el numero con mas cifras ha sido", numero_cifras_max,"con:",cifras_max, "cifras")            

while numero!=0:

    try:
    
        numero=int(input("Introduce un número"))
        numeros.append(numero)
        
    except Exception as e:
        print("No valido mete un numero",e)

cuenta_cifras(numeros)
print("adios")