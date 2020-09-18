def dividir(a, b):
    """
    Calcula a dividido b.
    Pre: a y b son números y b es distinto de cero.
    Post: Devuelve el número a dividido b.
    """
    assert b != 0, "No se puede dividir por cero."
    return a/b



def calcular_pago(cantidad, precio):
    """
    Calcula el costo total de una compra.
    Pre: cantidad y precio son números positivos.
    Post: devuelve el total de la compra.
    """
    assert cantidad > 0, "cantidad debe ser mayor a cero"
    assert precio > 0, "cantidad debe ser mayor a cero"
    return cantidad * precio

resultado = dividir(10,0)
print(resultado)
