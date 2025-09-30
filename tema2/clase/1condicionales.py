edad = int(input("Dime tu edad: "))
pais =input("Cual es tu pais: ")
if edad >= 18:
    print("Eres mayor de edad")
    print("mondongo")
    if pais == "esp":
        print("mayor de edad español")
elif edad >=12:
    print("Puedes pasar acompañado")
elif edad >=5:
    print("Puedes pasar acompañado de tus padres")
else:
    print("eres menor de edad")