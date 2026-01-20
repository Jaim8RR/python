import json
datos = ''' 
{
    "nombre":"Pepe",
    "telefono": {
        "tipo":"casa",
        "numero": "34-2334432234"
    }
}
'''
diccionario = json.loads(datos)
print("nombre", diccionario["nombre"])
print("numero telefono:", diccionario["telefono"]["numero"])