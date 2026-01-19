#Ejercicio3: Carrito de la compra
#Crea una clase en Python que simule un carrito de la compra.
#● Su atributo es una lista con los productos, siendo cada producto una tupla con
#nombre, cantidad y precio
#● Añade los siguientes métodos:
#○ aniadir_producto: Recibe los datos de un producto, y lo añade a la lista
#○ quitar_producto: Recibe el nombre de un producto, y lo quita de la lista
#○ importe_total: Retorna el importe total del carrito
#○ mostrar_carrito: Muestra el detalle de los productos del carrito, y una última
#línea con el importe total
#Prueba la clase instanciando un carrito, añade varios productos, y muestra el contenido.
#Elimina un producto del carrito, y vuelve a mostrar el contenido.

class Carro:
    def __init__(self):
        self.__carro =list()
    
    def __aniadir_producto(self,nombre,cantidad,precio):
        self.__carro.append((nombre,cantidad,precio))
    
    def quitar_producto(self,nombre):
        for producto in self.__carro:
            if producto[0] == nombre:
                self.__carro.remove(producto)
                break
    def importe_total(self):
        for producto in self.__carrito:
            total += producto[1] * producto[2]
        return total
    def mostrar_carrito(self):
        for producto in self.__carrito:
            print(f"\t- {producto[0]} Precio: {producto[2]} Cantidad: {producto[2]}")

        print(self.importe_total())
#Probando
carro = Carro()
carro.__aniadir_producto("patatas",5,2.55)
carro.__aniadir_producto("Manzanas",2,1.85)
carro.__aniadir_producto("Narankas",3,3.55)
carro.mostrar_carrito()
carro.quitar_producto("Narankas")
carro.mostrar_carrito()
