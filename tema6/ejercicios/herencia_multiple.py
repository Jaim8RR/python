class coche:
    def __init__(self,color,velocidadMaxima):
        self._color = color
        self._velocidadMaxima = velocidadMaxima
    def getColor(self):
        return self._color
    def setColor(self,color):
        self._color = color
    def getVelocidadMaxima(self):
        return self._velocidadMaxima
class barco:
    def __init__(self,nudosMaximos):
        self._nudosMaximos = nudosMaximos
    def getNudosMaximos(self):
        return self._nudosMaximos
    
class anfibio(coche,barco):
    def __init__(self, color, velocidadMaxima,nudosMaximos,marca,modelo,propietario=None):
        coche.__init__(self)
        barco.__init__(self)
        self.__marca = marca
        self.__modelo = modelo
        self.__propietario = propietario
        
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getPropietario(self):
        return self.__propietario
    def setPropietario(self):
        return self.__propietario

brumbrum = anfibio("Amphicar",770, "blanco", "112 km/h","7 nudos")
print(anfibio.getColor,anfibio.getMarca,anfibio.getModelo,anfibio.getNudosMaximos,anfibio.getVelocidadMaxima)
anfibio.setPropietario("presi lyndon")
anfibio.setColor("celeste")
print(anfibio.getColor,anfibio.getMarca,anfibio.getModelo,anfibio.getNudosMaximos,anfibio.getPropietario,anfibio.getVelocidadMaxima)


    