import socket
#creo mi socket para conectarme
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET indica que usaremos IPv4 y SOCK_STREAM indica que usaremos TCP
#me conecto al servidor
servidor = "httpbin.org"
puerto = 80
try:
    mi_socket.connect((servidor, puerto))#direccion y puerto del servidor
    print("Conexión exitosa")
    #envioa una petición HTTP GET
    cmd = "GET /get HTTP/1.1\r\nHost: httpbin.org\r\n\r\n"
    mi_socket.sendall(cmd.encode("utf-8"))
    #Obtengo la respuesta del servidor
    while True:
        datos = mi_socket.recv(512)
        if len(datos) < 1:
            break
        print(datos.decode("utf-8"))
except Exception as e:
    print("No se ha podido establecer la conexión:", e)

print("Fin de la conexión")
