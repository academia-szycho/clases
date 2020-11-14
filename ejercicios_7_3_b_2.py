"""
Ejercicio 7.3. Campaña electoral
b) Escribir una función que reciba una tupla con nombres,
una posición de origen p y una cantidad n, e imprima el mensaje 
"Estimado <nombre>, vote por mí." para los n nombres que se encuentran a 
partir de la posición p.
"""

def campana_electoral_mje_posicion(nombres,p,n):
    """
    Recibe una tupla con nombres, una posición de origen y una cantidad n,
    e imprime el mensaje "Estimado <nombre>, vote por mí." para los n
    nombres que se encuentran a partir de la posición p.
        Parameters:
                (tuple) De nombres.
                (int) Posición de origen en la tupla de nombres,
                      (de cual se quiere partir).
                (int) Una cantidad de nombres que se quieren imprimir,
                      a partir de la posición dada. Debo tener en cuenta,
                      la longitud de la tupla o dará error si el número es mayor.
        Returns: 
                (str) Imprime la cadena con el mje. para la cantidad de
                nombres ingresados que se encuentran a partir de la posición dada.
    """
    # n = p+n #Le sumo a la posición de la cual parto la cantidad de nombres que quiero imprimir
    assert p < len(nombres), "p sobrepasa la lista de nombres"
    assert p+n < len(nombres), "No hay tantos nombres para imprimir"

    m = min(p+n, len(nombres))
    for i in range(p,m):
        print(f"Estimado {nombres[i]}, vote por mí.")
    
campana_electoral_mje_posicion(("Plofi", "Gato", "Agus", "Connie", "Sabri", "Palo", "Martin"), 3, 7)
