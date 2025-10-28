#Haz un diccionario con los nombres de los estudiantes y su nota de programación.
#Muestra el estudiante con la mejor nota, y el estudiante con la peor nota
#Muestra la media aritmética de la clase y los nombres de los estudiantes cuyas notas son mejores que la media
notas = {
    "Jaime Dennise Riesgo Rossi" : 9,
    "Nicola Yuzy" : 6.9,
    "Migelon" : 5,
    "Joseph joestar" :10,
    "Enrique" :11,
    "Elias" :-1
}
media = 0
numero_alumnos = len(notas)
nota_max = 0
nombre_nota_max =""
nota_min = 11
nombre_nota_min =""
for clave in notas:
    media = media + notas[clave]
    if notas[clave] > nota_max:
        nombre_nota_max = clave
        nota_max = notas[clave]
    elif notas[clave] < nota_min:
        nombre_nota_min = clave
        nota_min = notas[clave]
    

    print(f"Clave: {clave} - Valor: {notas[clave]}")
print("Estudiantes con la menor nota :",nombre_nota_min,"con nota: ",nota_min)
print("Estudiantes con la mayor nota :",nombre_nota_max,"con nota: ",nota_max)
media = media/ numero_alumnos
print("media:", media)
print("Estudiantes por encima de la media")
for clave in notas:
    if media < notas[clave]:
        print(f"Alumno: {clave} - nota: {notas[clave]}")
