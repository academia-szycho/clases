"""
11 Manejo de archivos

Ejercicio 11.1. Escribir una función, llamada head que reciba un archivo y un número N e im-
prima las primeras N líneas del archivo.
"""

def head(archivo, n):
    """
    Imprime las primeras n lineas de archivo
    """
    with open(archivo, "r") as f:
        line = f.readline()
        i = 0
        while line != "" and i < n:
            print(line, end="")
            line = f.readline()
            i = i + 1