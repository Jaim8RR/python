#lee 3 enteros x y z(ancho, alto, profundo) que indican las dimensiones de un cuboide desde 0 a dichos valores incluidos y
#  otro entero llamado condicion
#imprime todas las cordenadas posibles, caras incluidas
#imprime las cordenadas donde x+y+z no es igual a condicion
#imprime el suelo del cuboide (y=0)
#imprime el techo del cuboide (ymaximo)

x = int(input("Dime el ancho (x): "))
y = int(input("Dime el alto (y): "))
z = int(input("Dime el profundo (z): "))
condicion = int(input("Dime la condicion: "))
#Cordenadas caras incluidas
cordenadas = [(i,j,k) for i in range(x+1) for j in range(y+1) for k in range(z+1)]
print("Cordenadas caras incluidas:")
print(cordenadas,"siendo un total de", len(cordenadas), "cordenadas")

#Cordenadas que no cumplen la condicion
cordenadas_no_condicion1 = [(i,j,k) for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != condicion]
print("Cordenadas que no cumplen la condicion (x+y+z != condicion):")
print(cordenadas_no_condicion1,"siendo un total de", len(cordenadas_no_condicion1), "cordenadas")
#cordenadas_no_condicion2 = [cordenada for cordenada in cordenadas if sum(cordenada) != condicion]
#print("Cordenadas que no cumplen la condicion (x+y+z != condicion) metodo 2:")
#print(cordenadas_no_condicion2,"siendo un total de", len(cordenadas_no_condicion2), "cordenadas")

#Cordenadas suelo (y=0)
print("Cordenadas del suelo (y=0):")
#usando las lista cordenadas ya creada(seria mas facil crearla directamente con la condicion)
print([cordenada for cordenada in cordenadas if cordenada[1] == 0])
#Cordenadas techo (y=maximo)
#usando las lista cordenadas ya creada
print("Cordenadas del techo (y=maximo):", y)
print([cordenada for cordenada in cordenadas if cordenada[1] == y])
#pared derecha (x=maximo)
print("Cordenadas de la pared derecha (x=maximo):", x)
print([cordenada for cordenada in cordenadas if cordenada[0] == x])





