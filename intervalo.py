class Intervalo:

    def __init__(self, desde, hasta):
        """
        :param desde: un número entero representado en segundos
        :param hasta: un número entero representado en segundos mayor a desde
        """
        assert desde < hasta, "desde debe ser menor que hasta"
        self._desde = desde
        self._hasta = hasta

    def get_desde(self):
        return self._desde
    
    def get_hasta(self):
        return self._hasta

    def duracion(self):
        return self._hasta - self._desde

    def interseccion(self, otro_intervalo):
        # [] ()
        # [(])
        # ([)]
        i2_desde = otro_intervalo.get_desde()
        i2_hasta = otro_intervalo.get_hasta()
        hasta = self.get_hasta()
        desde = self.get_desde()
        if hasta > i2_desde and hasta <= i2_hasta:
            # [()] o ([)]
            if desde <= i2_desde:
                # ([)]
                return Intervalo(i2_desde, hasta)
            else:
                # [()]
                return Intervalo(desde, hasta)
        else:
            # [] ()
            # [(])
            if desde > i2_desde and desde <= i2_hasta:
                # [(])
                return Intervalo(desde, i2_hasta)
            else:
                raise ValueError("No hay interseccion entre intervalos")
