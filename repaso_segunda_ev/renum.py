#EJERCICIO2: RENUM
#El lenguaje BASIC consta de varias líneas de instrucciones. Las líneas están numeradas
#(normalmente de 10 en 10 para que quepan otras intermedias), y tiene muchas instrucciones del tipo:
#150 GOTO 10 → El programa continúa la ejecución en la línea 10
#160 GOSUB 30 → El programa ejecuta la subrutina (función) de la línea 30
#que le dicen al programa que debe continuar la ejecución en la línea indicada (10, 30, etc).
#En el programa anterior, REM es comentarios, PRINT muestra un texto por consola, INPUT lee dos
#números A y B de la consola, SGN mira el signo de una resta (1 si positivo), GOTO sigue la ejecución
#en la línea indicada.
#La numeración tiene que ser ascendente y no repetida. A veces, de tanto añadir líneas por medio, no
#caben, y hay que renumerar todo el programa.
#Enunciado
#Vas a programar la utilidad RENUM, que renumera las líneas del programa para que vuelvan a
#quedar de 10 en 10. Ojo con los GOTO y los GOSUB!!
#La programación debe ser orientada a objetos.
#Nombre del programa: renum.py
#Entrada: Pide al usuario el nombre del programa basic, leerás el fichero para renumerarlo
#Proceso: Renumera de 10 en 10 las líneas del programa, y cambia los números que aparecen en las
#sentencias GOTO y GOSUB
#Salida: Imprime un fichero de salida que se llamará como el anterior terminado en R (de renum), y la
#extensión BAS.
#Pruebas: Prueba el programa con los ejemplos SUMA.BAS y con MAXCODIV.BAS
#SUMA.BAS
#20 PRINT "--- PROGRAMA DE SUMA CON SUBRUTINA ---"
#22 INPUT "Primer numero: ", A
#24 INPUT "Segundo numero: ", B
#25 GOSUB 30
#26 PRINT "EL RESULTADO OBTENIDO ES: "; SUMA
#27 END
#28 REM --- INICIO DE LA SUBRUTINA ---
#29 LET SUMA = A + B
#30 RETURN

#SUMAR.BAS
#10 PRINT "--- PROGRAMA DE SUMA CON SUBRUTINA ---"
#20 INPUT "Primer numero: ", A
#30 INPUT "Segundo numero: ", B
#40 GOSUB 70
#50 PRINT "EL RESULTADO OBTENIDO ES: "; SUMA
#60 END
#70 REM --- INICIO DE LA SUBRUTINA ---
#80 LET SUMA = A + B
#90 RETURN
