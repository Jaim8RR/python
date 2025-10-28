
texto = """La historia de Unicode es, en esencia, la búsqueda de una solución
al caos de la codificación de caracteres. Antes de Unicode, cada
idioma o sistema de escritura solía tener su propia codificación,
lo que generaba muchos problemas al intentar intercambiar
documentos o datos entre diferentes sistemas operativos o países.
Un texto escrito en un idioma podía aparecer como caracteres
incomprensibles en otro."""
texto =texto.replace(",","")
texto =texto.replace(" ","")
texto =texto.replace(";","")
texto =texto.replace(".","")
texto =texto.replace('"',"")
texto =texto.replace("-","")
texto =texto.replace("_","")
print(texto)
texto=texto.lower()
print(texto)
histograma = dict()
for letra in texto:
    if letra == "á":
        letra = "a"
    elif letra == "ó":
        letra = "ó"
    elif letra == "é":
        letra = "é"
    elif letra == "í":
        letra = "í"
    elif letra == "ú":
        letra = "ú"
histograma[letra] = letra
