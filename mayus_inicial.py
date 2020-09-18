def mayus_inicial(a):
    assert isinstance(a, str), "a debe ser una letra"
    assert len(a) == 1, "a debe ser solo una letra"
    return a.upper()