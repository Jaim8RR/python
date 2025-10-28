import socket
#creo mi socket para conectarme
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET indica que usaremos IPv4 y SOCK_STREAM indica que usaremos TCP
#me conecto al servidor
servidor = "www.google.com"
puerto = 80
try:
    mi_socket.connect((servidor, puerto))#direccion y puerto del servidor
    print("Conexión exitosa")
except Exception as e:
    print("No se ha podido establecer la conexión:", e)

print("Fin de la conexión")
