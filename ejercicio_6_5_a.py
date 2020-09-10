'''
Ejercicio 6.5. Escribir una función que dada una cadena de caracteres, devuelva:
b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
'república argentina' debe devolver 'República Argentina'.
'''

def abreviar(cadena):
    '''
    Devuelve la primera letra de cada palabra.

            Parameters:
                    cadena (string): una cadena de texto

            Returns:
                    (str): una cadena de texto con la primer letra de cada palabra
    '''
    lista_palabras = cadena.split(' ')
    abreviatura = ''
    for palabra in lista_palabras:
        abreviatura = abreviatura + palabra[0]

    return abreviatura

lista = abreviar("Universal Serial Bus")
print(lista)