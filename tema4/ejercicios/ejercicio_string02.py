cadena = "Hola"
contador = 1
contadorW = 0

print(len(cadena))

for letra in cadena:
 print("Elemento ", contador, " ",letra)
 contador+= 1

print("----------------------------------")
while True:
 print("Elemento ", contadorW, " ",cadena[contadorW])
 contadorW+= 1

 if contadorW == len(cadena):
    break
 



        