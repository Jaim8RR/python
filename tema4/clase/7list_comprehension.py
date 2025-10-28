#lista = [ expresion for item in iterable if condicion ]
#Ejemplo crear una lista con los cuadrados de los numeros pares entre 0 y 10
cuadrados = [x**2 for x in range(11) if x % 2 == 0]
print(cuadrados)
#Podemos simular for anidados obteniendo todas las combinaciones posibles
lista1 = [1,2,3]
lista2 = ['a','b','c']
combinaciones = [(a,b) for a in lista1 for b in lista2]
print(combinaciones)