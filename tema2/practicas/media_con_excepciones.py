# Ejercicio 2: Media con excepciones
import sys

seguir = True
total_numeros = 0
sumatorio_numeros = 0
numero_mas_pequenyo = sys.maxsize
numero_mas_grande = -sys.maxsize

while seguir:
    entrada = input("Di un número o fin:")
    if entrada == "fin":
        print("suma total: ",sumatorio_numeros)
        print("Cantidad de numeros: ",total_numeros)
        print("Numero mas grande:",numero_mas_grande)
        print("Numero mas pequeño:",numero_mas_pequenyo)
        print("La media de los numeros es: ",sumatorio_numeros/total_numeros)
        seguir = False
    else:
        try:
            numero = int(entrada)
            total_numeros += 1
            sumatorio_numeros += numero
            if numero > numero_mas_grande:
                numero_mas_grande = numero
            if numero < numero_mas_pequenyo:
                numero_mas_pequenyo = numero
        except Exception as ex:
            print(f"excepcion:{str(ex)} - y su mensaje: {type(ex).__name__}")
            print("Se pedia un numero no un texto (o fin)")
print("fin de codigo")

