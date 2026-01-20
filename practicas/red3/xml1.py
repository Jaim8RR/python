import xml.etree.ElementTree as ET

datos = '''
<persona>
    <nombre>Juan</nombre>
    <telefono tipo="casa">123456789</telefono>
</persona>

'''
arbol = ET.fromstring(datos)

print("Nombre:",arbol.find("nombre").text)
print("Tipo de telefono:",arbol.find("telefono").get("tipo"),"telefono;",arbol.find("telefono").text)

datos2 = '''
<agenda>
<persona>
    <nombre>Juan</nombre>
    <telefono tipo="casa">123456789</telefono>
</persona>
<persona>
    <nombre>Ana</nombre>
    <telefono tipo="movil">673589542</telefono>
</persona>
</agenda>
'''
arbol = ET.fromstring(datos2)
lista = arbol.findall("persona")

print("hay", len(lista)," elementos persona en el xml")
for elemento in lista:
    print("Nombre:", elemento.find("nombre").text)
    print("Tipo de telefono:", elemento.find("telefono").get("tipo"))
    print("Tipo de telefono:", elemento.find("telefono").text)