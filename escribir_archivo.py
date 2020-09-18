import os

dirname = os.path.dirname(__file__)
filename = "archivo_inexistente.txt"
# filename = "archivo_nuevo.txt"

f = open(os.path.join(dirname, filename), "w")
f.write("Hola mundo")
f.close()
