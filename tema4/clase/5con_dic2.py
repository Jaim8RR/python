dic = {
    "uno": "rojo",
    "dos": "azul",
    "tres": "verde",
    "cuatro": "cyan"
}
# recorrer diccionario
#por claves
for clave in dic:
    print(f"Clave: {clave} - Valor: {dic[clave]}")
print("########################")
#por valores
for valor in dic.values():
    print(f"Valor: {valor}")
print("########################")
#por claves y valores
for clave, valor in dic.items():
    print(f"Clave: {clave} - Valor: {valor}")