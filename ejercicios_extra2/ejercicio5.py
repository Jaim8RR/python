#Ejercicio 5
#Pide al usuario un número de inicio y un número de fin. Muestra la lista de números que cumplan la condición de que sean números de la tontería
#entre ese número de inicio y ese número de fin.
#Repite esta acción mientras que el número de inicio sea menor que el número de fin.
#Números de la tontería: Es un número que es igual a la suma de los sus cifras elevadas a la potencia igual al número que ocupan dentro del número
#como por ejemplo el 89. 8¹ + 9² = 89.

def numero_tonteria(numero):
    #print("numero tonteria de numero:", numero)
    elevados = list()
    numero_original = int(numero)
    for i in range(len(numero)):
        
        cifra = numero[i]
        potencia = i+1
        #print("cifra",cifra)
        #print("cifra elevada, a la potencia" ,potencia,"que es = ",(int(cifra)**(i+1)))
        
        elevados.append(int(cifra)**(i+1))
    #print(sum(elevados),"==", numero_original)
    #print(sum(elevados) == numero_original)
    return sum(elevados) == numero_original
    

    
        
    
        
        
    

while True:
    try:
        numero_inicio = int(input("Introduce un número de inicio: "))
        numero_fin = int(input("Introduce un número de fin: "))
        if numero_fin < numero_inicio:
            break
        for i in range(numero_inicio,numero_fin+1):

            if numero_tonteria(str(i)):
                print("Es nu numero tonteria: ",i)
                            
            
            
    except Exception as e:
        print("Excepción (probablemente no pusiste un número):", e)

