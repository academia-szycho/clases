class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


class Cuadrado(Rectangulo):
    
    def __init__(self, lado):
        super().__init__(lado, lado)