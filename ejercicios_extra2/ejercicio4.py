#Ejercicio 4
#A partir de las cifras de un número entero positivo obtén el número mayor y menor posible y
#muéstralos por pantalla. Tras ello al número mayor de los dos resultantes réstale el menor y
#comprueba si el resultado de esta operación es divisible entre 9.

#Ejemplo:

#Introduce un número entero positivo: 34187
#Salida
#● Número mayor: 87431
#● Número menor: 13478
#● Resultado de la resta: 73953
#● ¿73953 es divisible entre 9? Si

#Realiza esta operación hasta que el número introducido sea 0.
#Posteriormente muestra los números que no cumplan esta condición (la resta del número mayor y menor obtenida con sus cifras no sea divisible entre 9) entre 1 y 1.000.000.
numero = -1

#funcion que realiza la operacion
def operacion(numero):
    cifras = str(numero)
    mayor = sorted(cifras, reverse=True)
    menor = sorted(cifras)
    mayor = "".join(mayor) #junsta la lista en un string uniedo por ""
    menor = "".join(menor)
    resta = int(mayor) - int(menor)
    print(f"Número mayor: {mayor}")
    print(f"Número menor: {menor}")
    print(f"Resultado de la resta: {resta}")
    print(f"¿{resta} es divisible entre 9? {"Sí" if resta % 9 == 0 else "No"}")

while numero != 0:
    try:
        numero = int(input("Introduce un número entero positivo (0 para salir): "))
        if numero < 0:
            print("Por favor, introduce un número entero positivo.")
            continue
        if numero != 0:
            operacion(numero)
            
    except Exception as e:
        print("Excepción (probablemente no pusiste un número):", e)



