5 REM Algoritmo euclídeo para el cálculo del máximo común divisor
6 PRINT "Escribe dos enteros mayores que 0"
10 INPUT A,B
20 IF B=0 THEN GOTO 80
30 IF SGN(A-B) = 1 THEN GOTO 60
40 LET B=B-A
50 GOTO 20
60 LET A=A-B
70 GOTO 20
80 PRINT A
90 END