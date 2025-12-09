#Ejercicio 10
#Cifrado de Vigenère: Método polialfabético de sustitución que utiliza una palabra clave para
#cifrar un mensaje, desplazando cada letra del texto en función de la letra correspondiente de
#la clave.
#Cómo funciona:
#1.- Palabra clave: Se elige una palabra clave para cifrar el mensaje.
#2.- Repetición de la clave: Si la clave es más corta que el mensaje, se repite cíclicamente
#hasta que tenga la misma longitud.
#3.- Para cada carácter a cifrar: se suma el valor posicional de la letra del mensaje en claro y
#la letra de la clave, realizando la operación módulo 27 (para 27 letras del alfabeto).
# a = 0, b = 1, c = 2, ..., ñ = 14, ..., z = 26

#Haz un programa al que le pases un texto por parámetro y una clave. Deberá mostrar el
#criptograma correspondiente. Piensa a ver qué hacer con el descifrado y haz un programa
#para el descifrado también.
#Ten en cuenta esto para la obtención de los datos pasados como parámetros
import sys
alfabeto = {
    " ": " ",
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "ñ": 15,
    "o": 16,
    "p": 17,
    "q": 18,
    "r": 19,
    "s": 20,
    "t": 21,
    "u": 22,
    "v": 23,
    "w": 24,
    "x": 25,
    "y": 26,
    "z": 27
}



def cifrado_vigenere(texto,clave):
    print("cifrando", texto)
    #transformo el texto en numeros
    transformo_texto(texto,clave)
#    transformo_clave(len(texto),clave)

#def transformo_clave(len(texto),clave):
    

def descifrado_vigenere():
    print("tu texto sin cifrar")
    #transformo el texto en numeros


def transformo_texto(texto,clave):
    texto_transformado= list()
    clave_texto =list()
    contador =0
    for letra in clave:
        print(letra,"la letra")
        print(alfabeto.get(letra),"la letra en numero")
        clave_texto.append(str(alfabeto.get(letra)))
    print(clave_texto)
    for letra in texto:
        print(letra,"la letra")
        print(alfabeto.get(letra),"la letra en numero")
        texto_transformado.append(str(alfabeto.get(letra)+clave_texto[len(clave)%contador]))#
    print(texto_transformado)
        





if __name__ == "__main__":
    print("Paso parametros")
    print("Numero parametros",len(sys.argv))
    print(21//5)
    print(21%5)
    
    
    if len(sys.argv) !=1:
        texto = sys.argv[1]
        clave = sys.argv[2]
        opcion = input("Quieres encriptar o desencriptar? c/d: ")
        if opcion == "c":
            cifrado_vigenere(texto,clave)
        elif opcion == "d":
            descifrado_vigenere()
    else:
        print("sin parametros")


