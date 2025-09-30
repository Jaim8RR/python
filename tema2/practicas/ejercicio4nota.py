nota = float(input("Dime tu nota: "))

if nota >10 or nota <0:
    print("nota fuera de rango")
if nota == 0 or 1 or 2 or 3:
    print(nota, "Muy deficiente")
elif nota >= 4:
    print(nota, "Muy deficiente")
elif nota >= 5:
    print(nota, "Muy deficiente")
elif nota >= 6:
    print(nota, "bien")
elif nota >= 7:
    print(nota, "notable")
elif nota >= 9:
    print(nota, "Sobresaliente")

