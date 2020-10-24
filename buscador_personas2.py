import os

dirname = os.path.dirname(__file__)
filename = "personas.csv"
try:
    f = open(os.path.join(dirname, filename), "r")
except FileNotFoundError:
    print("archivo no encontrado")
    exit()

personas = {}

try:
    linea = f.readline()
    while linea:
        lista_persona = linea.split(",")
        personas[lista_persona[0]] = linea
        # trabajo con la personas
        linea = f.readline()
    
except ValueError as e:
    print("Error de valores: revise que el archivo tenga 3 líneas como mínimo.")
finally:
    print("Terminé el procesamiento del archivo")

nombre_persona_a_buscar = input("Introduzca el nombre a buscar: ")

print(personas[nombre_persona_a_buscar])