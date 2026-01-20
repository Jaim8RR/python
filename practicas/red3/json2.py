import json
# Este JSON es un array de objetos
datos = '''
[
{
"nombre": "Pepe",
"telefono": "91222222"
},
{
"nombre": "Pepe",
"telefono": "91222222"
}
]
'''
# loads() parsea el JSON y lo guarda en una lista de diccionarios
lista = json.loads(datos)
# Recorro la lista para mostrar los datos de cada diccionario
for diccionario in lista:
    print("Nombre:",diccionario["nombre"])
    print("\tTeléfono:",diccionario["telefono"])