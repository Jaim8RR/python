import random

seguir_jugando = True

while seguir_jugando:
    n1 = 1
    n2 = 10
    numero_adivina = random.randint(n1, n2)
    print(numero_adivina)  # para saber cual es

    numero_acertado = False
    while not numero_acertado:
        numero_user = int(input("Dime un número entre el 1 y 10: "))
        if 1 <= numero_user <= 10:
            if numero_user == numero_adivina:
                numero_acertado = True
                print("¡Acertaste! El número era:", numero_adivina)
            elif numero_user > numero_adivina:
                print("El número es menor")
            else:
                print("El número es mayor")
        else:
            print("Número fuera de rango")

    # Preguntar si quiere seguir
    
    while True:
        pregunta_seguir_jugando = input("¿Quieres seguir jugando? (S/N): ").lower()
        if pregunta_seguir_jugando == "n":
            print("Terminamos el programa.")
            seguir_jugando = False
            break
        elif pregunta_seguir_jugando == "s":
            break
        else:
            print("Opción no válida, responde S o N.")
            
print("Fin del programa")
