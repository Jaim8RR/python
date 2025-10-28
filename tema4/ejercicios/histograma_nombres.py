#Los nombres de pila suelen seguir tendencias y modas… es habitual que en un aula haya
#un nombre bastante repetido.
#Vamos a estudiar cuál es el nombre más frecuente de un aula, con los siguientes alumnos:
#Pepe, Ana, Alex, María, Silvia, Dany, Alex, Ana, Carlos, Juan, Dany, Carlos, Sara, Adnan,
#Andrés, Alex, Ana, Nacho, Mar, Nico
#En este ejercicio vamos a calcular cuánto se repiten los nombres en una clase del instituto.
#Pag: 20
#Programación en Python
#Para ello:
#● Guardaremos todos los nombres en una lista.
#● Crearemos un diccionario, donde almacenaremos la frecuencia de cada nombre, es
#decir, el número de veces que se repite cada nombre, es decir, el histograma.
#● Mostraremos el histograma:Cada nombre y el número de veces que se repite
nombres =["Jaime","Jaime","Juan","Estabanco","Mario","Ana","David","Mario","Yusuf","Hideo","Esteban","Nico","Ana"]
dict = dict()
for nombre in nombres:
    if nombre in dict:
        dict[nombre] += 1
    else:
        dict[nombre] =1
for clave, valor in dict.items():
    print(f"Nombre: {clave} - Veces que se repite: {valor}")

    
