class Alumno:
            
    def __init__(self,nombre, correctas, resultado):
        self.nombre = nombre
        self.correctas = 0
        self.resultado = None
        self.examenes = []
        
    def agregar_examen(self, examen):
        self.examenes.append(examen)
    
    def get_examen(self):
        return self.examenes.append
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_correctas(self):
        return self.correctas
    
    def set_correctas(self, correctas):
        self.correctas = correctas

    def get_resultado(self):
        return self.resultado
    
    def set_resultado(self, resultado):
        self.resultado = resultado

    def imprimir_alumno(self):
        print(self.nombre, self.correctas, self.resultado)
        
def imprimir_alumnos(alumnos):
    for alumno in alumnos:
        alumno.imprimir_alumno()

alumno1 = Alumno("Plofi",8,"Aprobado")
alumno2 = Alumno("Gato", 7,"Aprobado")
alumnos = [alumno1,alumno2]

imprimir_alumnos(alumnos)