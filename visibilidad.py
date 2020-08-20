alumnos_noche = ["Gabo", "elwachopiola", "Gise", "Manu Manu", "Mauro19Hz"]
alumnos_tarde = []

def agregar_alumno(alumnos, alumno):
    alumnos = []
    alumnos.append(alumno)
    return alumnos

alumnos_noche = agregar_alumno(alumnos_noche, "mbellesi")
alumnos_noche = agregar_alumno(alumnos_noche, "Nicky")

print(alumnos_noche)
print(alumnos_tarde)
