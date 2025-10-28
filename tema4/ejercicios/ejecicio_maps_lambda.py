

n_alumnos = int(input("Dime el numero de alumnos: "))
calificaciones = input("Dime las notas (separadas por espacios): ")

#Separo por espacios
calificaciones.split()
try:
	lista_calificaciones = list( calificaciones.split())
	for nota in lista_calificaciones:
        #quito los espacios en blanco
		nota = nota.strip()
	#SEGUNDA NOTA MAS ALTA
	print("La segunda nota mas alta es:", sorted(set(lista_calificaciones))[-2])
except ValueError:
	print("Error: las notas deben ser números separados por espacios.")
if len(lista_calificaciones) != n_alumnos:
	print(f"Advertencia: número de notas ({len(lista_calificaciones)}) distinto de número de alumnos ({n_alumnos})")


print(lista_calificaciones)


