import urllib.request, urllib.parse , urllib.error
import xml.etree.ElementTree as ET
h_fichero = urllib.request.urlopen("https://mocktarget.apigee.net/xml")
xml = h_fichero.read().decode()
#print(xml)
arbol = ET.fromstring(xml)
print("ciudad",arbol.find("city").text)
print("estado",arbol.find("state").text)