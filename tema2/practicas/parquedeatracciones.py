
altura = float(input("Dime tu estatura(em metros): "))


#si es mayor a 10 puede ir solo
if altura > 1.50:
    edad = int(input("Dime tu edad: "))
    if edad <= 18:
        acompañado = str(input("Vas acompañado? si/no :"))
        if acompañado == "si":
            edadAcompañante = int(input("edad del acompañante?"))
            if edadAcompañante >= 18:
                print("puedes pasar")
        if acompañado == "no":
            if edad>10:
                print("puedes pasar")
    else: print("no puedes pasar")
else: print("No puedes pasar enano")
            
                
                
