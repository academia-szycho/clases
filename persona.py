class Persona:
    # atributos de clase
    ROJO = "ROJO"
    NEGRO = "NEGRO"
    AZUL = "AZUL"

    colores_validos = [ROJO, NEGRO, AZUL]

    # constructor
    def __init__(self, nombre, apellido, edad, altura, posicion=0, color_pelo=ROJO):
        # atributos de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.posicion = posicion
        self.color_pelo = color_pelo

    # métodos 
    def moverse(self, pasos):
        self.posicion += pasos

    def mostrar_posicion(self):
        for casillas in range(self.posicion):
            print("_________ ", end="")
        print(self.nombre)

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    # método de clase
    @staticmethod
    def validar_color(color):
        for color_valido in Persona.colores_validos:
            if color_valido == color:
                return color
        return Persona.NEGRO
    

nombre = "Gabo"
apellido = "Lato"

persona1 = Persona(nombre, apellido, 33, 1.75, 0)
persona2 = Persona("Plofi", "Bur", 35, 1.5, 1)
personas = [persona1, persona2, Persona("Oscar", "Vasta", 35, 1.75, 2)]

def mostrar_personas(personas):
    for persona in personas:
        persona.mostrar_posicion()

mostrar_personas(personas)

persona1.moverse(3)

mostrar_personas(personas)

persona4 = Persona("XXX", "YYY", 23, 1.6, 0, 2)

personas.append(persona4)

mostrar_personas(personas)

print(persona1.nombre)