class Perro:
    #Atributos de CLASE
    especie = "perro"

    #Contructor
    def __init__(self,nombre,colorPelo=None):
        #Inicializo todos los atributos de OBJETO
        self.nombre = nombre
        self.colorPelo = colorPelo
        self.peso = None

    #destructor
    def __del__(self):
        print("Objeto eliminado")
    def ladrar(self):
        print("guau")
    def describir(self):
        print("Me llamo",self.nombre)
        print("Soy un", Perro.especie)
        
        #Codigo más seguro (autocorreccion)
        if hasattr(self,"colorPelo") and self.colorPelo is not None:
            print("Mi color de pelo es ",self.colorPelo)
        if hasattr(self,"peso") and self.peso is not None:
            print("Mi peso es ",self.peso)
#Pruebo la clase
bartek = Perro("Bartolo","Rubio")
bartek.describir()
bartek.ladrar
del bartek
truco = Perro("truquito","tricolor")
truco.peso = 6.45

truco.describir()
truco.ladrar()

