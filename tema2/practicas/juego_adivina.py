seguir_jugando = True
import random
#se genera el numero aleatorio del programa:
while seguir_jugando:
    n1 = 1
    n2 = 10
    numero_adivina = random.randint(n1,n2)
    print(numero_adivina)
    numero_no_en_rango = True
    numero_user = -1
    numero_acertado = False
    while numero_no_en_rango and not(numero_acertado):#not es el ! de java
        numero_user = int(input("Dime un numero entre el 1 y 10 "))
        if numero_user > 0 and numero_user < 11:
            numero_no_en_rango = False
            if numero_user == numero_adivina:
                numero_acertado = True
                print("acertaste el numero era: ",numero_adivina)
            if numero_user > numero_adivina:
                print("el numero es menor")
            if numero_user < numero_adivina:
                print("el numero es mayor")
        else:
            print("numero fuera de rango")
            
    pregunta_seguir_jugando = ""
    opcion_valida =True
    while opcion_valida:
        pregunta_seguir_jugando = str(input("Quieres seguir jugando? S/N"))
        if pregunta_seguir_jugando.lower == "n" or pregunta_seguir_jugando.lower == "s":
            opcion_valida=True
        else: 
            opcion_valida= False
        if pregunta_seguir_jugando.lower == "n":
            print("no sigo jungando")
            seguir_jugando = False
print("fin del programa")