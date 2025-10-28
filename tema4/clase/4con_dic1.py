dic = {"clave1": "valor1", "clave2": "valor2" , 3 : 45 , 5 : [1,2,3]}
print(dic)
print(dic["clave1"])
print(dic[3])
#metodos
print(dic.get("clave2"))#otra forma de acceder al valor , si no existe devuelve None , si le pasamos un segundo parametro lo devuelve en lugar de None

#in
if "clave1" in dic:
    print("existe clave1 en el diccionario")

# para valores
if "valor2" in dic.values():
    print("existe valor2 en el diccionario")
#añadir o modificar
dic["nueva_clave"] = "nuevo_valor"
print(dic)
dic["nueva_clave"] = "valor_modificado"
print(dic)
#metodos: pop, del, clear
dic.pop("clave2") 
print(dic)
del dic["clave1"]
print(dic)
dic.clear()
print(dic)




