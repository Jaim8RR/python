class Fiesta:
    def __init__(self,nombre,lugar):
        self.__nombre = nombre
        self.__lugar = lugar

    def getNombre(self):
        return self.__nombre
    def getLugar(self):
        return self.__lugar
    
class FiestaTematica(Fiesta):
    def __init__(self,nombre,lugar,tema):
        super().__init__(nombre,lugar)
        self.__tema = tema

    def getTema(self):
        return self.__tema
#Pruebo la clase
fiesta_romana = FiestaTematica("Fiesta de dosfraces Romana","Mi casa","Romana")
print("Nombre de la fiesta:",fiesta_romana.getNombre())
print("Lugar de la fiesta:",fiesta_romana.getLugar())
print("Tema de la fiesta:",fiesta_romana.getTema())     

