'''
Ejercicio 7.3. Campaña electoral
b) Escribir una función que reciba una tupla con nombres, una posición de origen p y una
cantidad n, e imprima el mensaje anterior (Estimado <nombre>, vote por mí.)
para los n nombres que se encuentran a partir de la posición p.
'''

def ejercicio_siete(nombres, origen_p, n):
    '''
    '''
    n = origen_p + n #Le sumo a la posición de la cual parto la cantidad de nombres que quiero imprimir.
    
    for i in range(origen_p, n):
        print(f"Estimado {nombres[i]}, vote por mí.")


nombres = ("Plofi", "Gabo", "Maty", "Oscar")

ejercicio_siete(nombres, 0, 1)
