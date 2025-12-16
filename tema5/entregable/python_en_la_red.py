#2.3.- Ejercicio: Obtener páginas web con urllib
#Haz un programa python que, mediante la librería urllib, obtenga la página web (sin expresiones regulares):
#https://www.example.com/
#y realice las siguientes operaciones:
#1. Muestre el HTML recibido en la consola
#2. Muestre el número de caracteres recibidos
#3. Muestre las etiquetas utilizadas y cuántas veces ha utilizado cada una. Entendemos
#por etiqueta <h1>, pero no su correspondiente etiqueta de cierre. No mostrarás
#ninguna etiqueta del head (<meta>, <style>, <title>, etc)
#4. Escriba el HTML recibido en el fichero recuperado.html
#Abre el texto recuperado.html con un navegador y comprueba que es similar a navegar a la
#página directamente desde un navegador.
import urllib.request, urllib.parse , urllib.error
h_fichero = urllib.request.urlopen("https://www.example.com/")
html = h_fichero.read().decode()
print("HTML: ",html)
print("TOTAL CARACTERES: ",len(html))

etiquetas = {}
for letra in range(len(html)):
    if html[letra] == "<" and html[letra+1] != "/" and html[letra+1] != "!":#si no cerramos una etiqueta(es decir la abrimos)+
        etiqueta = ""
        for i in range(len(html)+letra):
            
            #print("compararo:",html[i+letra])
            if html[i+letra] != ">" and html[i+letra] != " ":
                if html[i+letra] != "<":
                    etiqueta = etiqueta+html[i+letra]
            else:
                break
        #print("la etiqueta es:",etiqueta)
        if etiqueta in etiquetas:
            etiquetas[etiqueta] += 1
        else:
            etiquetas[etiqueta] = 1
for tag in etiquetas:
    if tag != "meta" and tag != "style" and tag != "title":
        print(tag," : ",etiquetas[tag])
try:
    with open("recuperado.html","w") as  fSalida:
        fSalida.write(html)
except Exception as e:
    print(e)






#print(html)


