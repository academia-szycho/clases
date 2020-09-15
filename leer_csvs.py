import os

dirname = os.path.dirname(__file__)
filename = "nombres.csv"

f = open(os.path.join(dirname, filename), "r")

encabezado = []
encabezado.append(f.readline().split(","))

nombres = []
(nombre, apellido) = f.readline().split(",")
nombres.append((nombre, apellido))

(nombre, apellido) = f.readline().split(",")
nombres.append((nombre, apellido))

for nombre in nombres:
    print(f"Nombre: {nombre[0]} - Apellido: {nombre[1]}.")