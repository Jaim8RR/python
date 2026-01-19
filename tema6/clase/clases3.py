class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salario = 1800
        
    #getter y setters
    def getNombre(self):
        return self.nombre
    def getSalario(self):
        return self.salario
    def setSalario(self, salario):
        self.__salario = salario
#Pruebo la clase
pepe = Empleado("Pepe Garcia")
pepe.setSalario(2000)
print(pepe.getNombre(),"Cobra:",pepe.getSalario())