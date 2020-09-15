
def contar_coincidencias(lista_donde_buscar, elemento_a_buscar):
    """
    Devuelve la cantidad de coincidencias entre elemento_a_buscar y los elementos de lista_donde_buscar.
    Returns:
        int: cantidad de coincidencias.
    """
    cont = 0
    for elemento in lista_donde_buscar:
        if elemento == elemento_a_buscar:
            cont = cont + 1
    return cont