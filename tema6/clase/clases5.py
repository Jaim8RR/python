class Animal_volador:
    def vuela(self):
        print("Estoy volando")
class Animal_nadador:
    def nada(self):
        print("Estoy nadando")
class Pato(Animal_volador,Animal_nadador):
    def __init__(self,nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre
    def cuac(self):
        print("Cuac Cuac")
#Pruebo la clase
donald = Pato("Donald")
print("Mi nombre es ",donald.getNombre() )
donald.cuac()
donald.vuela()
donald.nada()
