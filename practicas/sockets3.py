import socket
#creo mi socket para conectarme
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET indica que usaremos IPv4 y SOCK_STREAM indica que usaremos TCP
#me conecto al servidor
servidor = "data.pr4e.org"
puerto = 80
protocolo = "HTTP/1.1"
get = "http://data.pr4e.org/romeo.txt"
contador =0
try:
    mi_socket.connect((servidor, puerto))#direccion y puerto del servidor
    print("Conexión exitosa")
    #envioa una petición HTTP GET
    cmd = f"GET {get} {protocolo}\r\nHost: {servidor}\r\n\r\n"
    mi_socket.sendall(cmd.encode())
    #Obtengo la respuesta del servidor
    while True:
        datos = mi_socket.recv(512)
        if len(datos) < 1:
            break
        contador += 1
        print(datos.decode(), end="")
except Exception as e:
    print("No se ha podido establecer la conexión:", e)

print("Fin de la conexión, veces recibidas:",contador)
