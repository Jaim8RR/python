#Ejercicio 4: Restaurante
#Haz una clase Restaurante, con los siguientes elementos:
#● Atributos:
#○ Platos del menú: Es un diccionario con pares “nombre”: precio
#○ Reservas: Es una lista con las mesas reservadas. Cada mesa se identifica
#por un número
#○ Pedidos: Es una lista de diccionarios. Cada elemento de la lista (diccionario)
#contiene dos entradas, el número de mesa y el producto. Habrá tantos
#elementos como productos se pidan en las mesas.
#● Métodos:
#○ Un constructor que inicializa los atributos de la clase
#○ Añadir elemento al menú: Añade un elemento al atributo con los platos del
#menú
#○ Reservar mesa: Se añade la mesa indicada a las reservas
#○ hacer pedido: Se añade un pedido a la lista de pedidos, con los datos
#número de mesa que hace el pedido y nombre del producto solicitado
#○ mostrar menu: Este método mostrará los platos del menú
#○ mostrar reservas: Este método mostrará las mesas reservadas hasta el
#momento
#○ mostrar pedidos: Este método mostrará los pedidos de cada mesa,
#ordenados por número de mesa

class Restaurante:
    def __init__(self):
        self.__platos_menu = dict()
        self.__resevas = list()
        #self.__lista_pedidos = dict()
        self.__pedidos = list()
    def add_plato(self,nombre,precio):
        self.__platos_menu[nombre] = precio
    def reservar_mesa(self,n_mesa):
        self.__resevas.append(n_mesa)
    def hacer_pedido(self,mesa,plato):
        pedido= dict()
        pedido["mesa"] = mesa
        pedido["plato"] = plato
        self.__pedidos.append(pedido)
    def mostrar_menu(self):
        print("Menu:")
        for nombre,precio in self.__platos_menu.items():
            print(f"\t- {nombre}: {precio}")
    def mostrar_reservas(self):
        print("Reservas:")
        for mesa in self.mostrar_reservas:
            print("-",mesa)
            
    def mostrar_pedidos(self):
        print("pedidos")
        lista = list()
        for pedido in self.__pedidos:
            lista.append((pedido["mesa"], pedido["plato"]))
        lista.sort()
        for mesa,plato in lista:
            print(f"\t - Mesa {mesa} : {pedido} ")

#probandp

foster = Restaurante()
foster.add_plato("Costillar",17.95)
foster.add_plato("Hamburgesa",7.99)
foster.add_plato("Helado",3.99)
foster.add_plato("Cocacola",1.99)
foster.reservar_mesa(1)
foster.reservar_mesa(3)
foster.reservar_mesa(4)
foster.hacer_pedido(1,"Costillar")
foster.hacer_pedido(3,"Hamburgesa")
foster.hacer_pedido(1,"Costillar")
foster.hacer_pedido(4,"Helado")
foster.hacer_pedido(4,"cocacola")
foster.mostrar_menu()
foster.mostrar_pedidos()
foster.mostrar_reservas()
