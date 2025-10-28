cadena = "Hola mundo"
print(cadena[:])
dos = cadena + " " + cadena
print(dos)

if (cadena == dos):
    print("iguales")
else:
    print("distintos")


cad1 = "Hola"
cad2 = "HOLA"

cad2 = cad2.capitalize()

if(cad1 == cad2):
    print("Iguales")
elif(cad1 > cad2):
    print("cad1 es mayor, va después")
elif (cad2 > cad1):
    print("cad2 es mayor, va después")

#print(type(cad1))
#print(dir(cad1))
cadena = "Entretenido"
print("El en está en la posicion: ", cadena.find('en'))
print(cadena[cadena.find('en'):])
cadena = "Estamos en el Europa, que es un insti de Europa"
cadena = cadena.replace("Europa", "Madrid")
print(cadena)
cadena = "     hola      "
print(cadena.strip())