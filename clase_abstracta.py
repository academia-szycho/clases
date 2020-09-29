import abc

class Ave(abc.ABC):

    x = 0
    nombre = ""

    def vuela(self):
        pass

    def mostrar_posicion(self):
        print(self.nombre, self.x)

class Perico(Ave):

    velocidad = 48
    nombre = "Perico"

    def __init__(self):
        self.x = 0

    def vuela(self):
        self.x += self.velocidad
    
class Aguila(Ave):

    velocidad = 275
    nombre = "Aguila"

    def __init__(self):
        self.x = 0

    def vuela(self):
        self.x += self.velocidad
        self.velocidad += 1