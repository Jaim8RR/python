import urllib.request, urllib.parse , urllib.error
import json
h_fichero = urllib.request.urlopen("https://mocktarget.apigee.net/json")
datos = h_fichero.read().decode()
#print(datos)
diccionario = json.loads(datos)
print("nombre", diccionario["firstName"])
print("apellido", diccionario["lastName"])
