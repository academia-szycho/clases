'''
Ejercicio 6.5. Escribir una función que dada una cadena de caracteres, devuelva:
b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
'república argentina' debe devolver 'República Argentina'.
'''

def titular(cadena):
    '''
    Devuelve la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
    'república argentina' debe devolver 'República Argentina'.

            Parameters:
                    cadena (string): una cadena de texto

            Returns:
                    (str): una cadena de texto con la primer letra de cada palabra en mayúscula
    '''
    return cadena.title()

lista = titular("repúBlica argentina")
print(lista)


