#Pide al usuario su nombre con el formato “apellido1, apellido2, nombre”, y luego imprime un saludo con su nombre de pila.
nombre_completo = input("Introduce nombre y apellidos: ")
apellidos_nombre=nombre_completo.split(",")
print("hola",apellidos_nombre[len(apellidos_nombre)-1])
