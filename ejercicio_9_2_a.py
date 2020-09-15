'''
Ejercicio 9.2. Diccionarios usados para contar.
a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que
hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.
'''

def reemplaza_tildes(palabra):
    """
    Devuelve la palabra sin tildes.
            Parameters:
                    cadena (string): una cadena de texto
            Returns:
                    (str): la misma cadena sin tildes
    """

def contar_palabras(cadena):
    """

    """
    palabras = cadena.split(" ")
    contador = {}
    for palabra in palabras:
        palabra = palabra.lower()
        contador_actual = contador.get(palabra, 0)
        contador[palabra] = contador_actual + 1
    return contador

resultado = contar_palabras("Qué lindo día que hace hoy")
print(resultado)