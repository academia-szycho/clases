class Auto:

    def __init__(self, velocidad=60, color="negro", cant_puertas=3):
        self._velocidad = velocidad
        self._color = color
        self._cant_puertas = cant_puertas


    def __str__(self):
        return (f"Velocidad: {self._velocidad}, Color: {self._color}, "
                f"cantidad de puertas: {self._cant_puertas}")


auto = Auto()

print(auto)