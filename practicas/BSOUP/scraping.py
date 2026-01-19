import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#Con urlllib obtengo la pagina
url = input("Dime una pagina:")
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")

etiquetas = soup("a")
for etiqueta in etiquetas:
    print(etiqueta.get("href", None))

