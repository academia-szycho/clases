import os
from ejercicio_11_1 import head

dirname = os.path.dirname(__file__)
filename = "hola_que_tal.txt"

head(os.path.join(dirname, filename), 4)