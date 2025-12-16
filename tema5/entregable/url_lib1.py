import urllib.request, urllib.parse , urllib.error

h_fichero = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

for linea in h_fichero:
    print(linea.decode() , end="")
