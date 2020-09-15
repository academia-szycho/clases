'''
Ejercicio 6.5. Escribir una función que dada una cadena de caracteres, devuelva:
b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
'república argentina' debe devolver 'República Argentina'.
'''

def mayuscula(cadena):
    '''
    Devuelve la primera letra de cada palabra.
            Parameters:
                    cadena (string): una cadena de texto
            Returns:
                    (str): una cadena con la primera letra de cada palabra en mayúsculas
    '''

    lista_palabras = cadena.split(" ")
    nueva_frase = []
    for palabra in lista_palabras:
        primera_letra = palabra[0]
        nueva_palabra = primera_letra.upper() + palabra[1:]
        nueva_frase.append(nueva_palabra)
    return " ".join(nueva_frase)

lista = mayuscula("república argentina")
print(lista)


