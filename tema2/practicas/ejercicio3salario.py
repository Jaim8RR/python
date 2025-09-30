horas_trabajadas = int(input("introduce horas trabajadas: "))
salario_hora = float(input("introduce el precio de tu hora: "))
if horas_trabajadas <= 40:
    salario = salario_hora * horas_trabajadas
else:
    horas_extra = horas_trabajadas -40
    salario = salario_hora * 40 + horas_extra * salario_hora *1.5
print("Tu salario seran:", salario)