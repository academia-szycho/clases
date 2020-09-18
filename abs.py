def abs(i):
    """
    Devuelve el valor absoluto del número recibido.
    Parameters
        i: int
            Es un número.
    Returns
        int
            El valor absoluto de i
    """
    assert isinstance(i, (float, int)), "i debe ser un número"
    if i >= 0:
        return i
    else:
        return -i