'''
PRÁCTICA 4: Cóckteles 
Módulo: Programación en Python 

Enunciado:
1. Investiga los servicios (API) gratuítos que ofrecen
2. Encuentra el enlace que te proporciona un cocktail gratuíto. Estudia el interface de este servicio.
3. Haz un programa que se conecte con urllib a dicho servicio:
    a. Obten los datos que retorna la API, en formato string
    b. Parsea el string en una estructura de datos Python adecuada
    c. Muestra el nombre, datos sobre la bebida, los ingredientes y las cantidades, y la receta (Español/Inglés).
    d. Guarda esta información en un fichero .txt en "./cockteles". Nombre: "id - nombre".
    e. Obtén la imagen del cocktail.
    f. Guarda la imagen en "./cockteles/img" con el mismo nombre y extensión .jpg. 
       Nota: Fichero binario (wb), no utf-8.
'''

import urllib.request, urllib.parse, urllib.error 
import json
import os #para crear las carpetas

#ruta de la api para un random
url_api = "https://www.thecocktaildb.com/api/json/v1/1/random.php" # ek 1 despues de v1 es la key gratuita de desarrollador

respuesta = urllib.request.urlopen(url_api)
# Leo y decodifico a string para poder tratarlo como texto
datos = respuesta.read().decode() 


# Convierto el string que ha llegado en un diccionario
# Referencia: json.loads() en json2.py
diccionario_completo = json.loads(datos)
#print("Datos parseados de la API:" , diccionario_completo)


#devuelve un diccionario con una lista llamada "drinks".
# Tengo que coger la posición 0 de esa lista.
cocktail = diccionario_completo["drinks"][0]
#print("Cocktail obtenido:", cocktail)
# datos que me interesan
id = cocktail["idDrink"]
nombre = cocktail["strDrink"]
categoria = cocktail["strCategory"]
vaso = cocktail["strGlass"]
alcohol = cocktail["strAlcoholic"]

# ternario para instrucciones en español o inglés
instrucciones = cocktail["strInstructionsES"] if cocktail["strInstructionsES"] else cocktail["strInstructions"]


# como son claves sueltas me hago yo una lista , es mentira me he hecho un string xd

# Hago un bucle for del 1 al 16 para recorrerlos todos.
texto_ingredientes = ""

for i in range(1, 16):
    #creo las claves segun su numero
    clave_ing = "strIngredient" + str(i)
    clave_medida = "strMeasure" + str(i)
    
    # Saco el ingrediente del diccionario
    ingrediente_actual = cocktail[clave_ing]
    if ingrediente_actual:#si hay ingrediente
        medida = cocktail[clave_medida]
        # A veces la medida viene None, lo cambio por cadena vacía para que no falle al sumar strings
        if medida is None:
            medida = ""
        texto_ingredientes += "  " + ingrediente_actual + ": " + medida + "\n"

# Monto el string final que voy a imprimir y guardar
#resultado_final = "ID: " + id + "\n"
resultado_final = "Nombre: " + nombre + "\n"
resultado_final += "Categoria: " + categoria + " - " + alcohol + "\n"
resultado_final += "vaso: " + vaso + "\n"
resultado_final += "\nIngredientes:\n" + texto_ingredientes
resultado_final += "\nInstrucciones:\n" + instrucciones + "\n"

print(resultado_final)

#guardado en fichero
# creo la carpeta si no existe
if not os.path.exists("./cockteles"):
    os.makedirs("./cockteles")


nombre_archivo = id + " - " + nombre
ruta_txt = "./cockteles/" + nombre_archivo + ".txt"

#abro fichero
fichero_txt = open(ruta_txt, "w", encoding="utf-8")
fichero_txt.write(resultado_final)#reutilizo lo del print
fichero_txt.close()
print("Receta guardada en:", ruta_txt)

#foto
url_foto = cocktail["strDrinkThumb"]
respuesta_img = urllib.request.urlopen(url_foto)
datos_imagen = respuesta_img.read()

# creo la carpeta si no existe
if not os.path.exists("./cockteles/img"):
    os.makedirs("./cockteles/img")

ruta_jpg = "./cockteles/img/" + nombre_archivo + ".jpg"

# wb = write binary
fichero_img = open(ruta_jpg, "wb")
fichero_img.write(datos_imagen)
fichero_img.close()