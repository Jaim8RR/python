lista = [1,54 ,3 ,7, "abuelo"]
for elemento in lista:
    print(elemento)

lista2 = [1,2,3,4,5,6,7,8,100,-200]
maximo = None
minimo = None
numero_elementos = 0
suma_total = 0
suma_positivos = 0
for numero in lista2:
    print(numero)
    numero_elementos += 1
    if numero >0:
        suma_positivos = suma_positivos + numero
    if maximo < elemento:
        maximo = elemento
    if minimo > elemento:
        minimo = elemento
print(f"hay {numero_elementos} elementos en la lista")
print("El maximo numero de los elementos es :", maximo ," y el minimos es :", minimo)
print("la suma es:", suma_total)
print("la media es", suma_total/numero_elementos)
print("Los numeros positivos sumados es:", suma_positivos)
