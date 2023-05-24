from modelo.vivienda import Vivienda


class Viviendaenedificio(Vivienda):
    def __init__(self, numero_de_identificacion, estado_de_terminacion, fecha_inicio, cantidad_metros_cuadrados, cantidad_de_cuartos, direccion,  piso, balcon, nro_edificio, cantidad_pisos):
        Vivienda.__init__(self, numero_de_identificacion, estado_de_terminacion, fecha_inicio, cantidad_metros_cuadrados, cantidad_de_cuartos, direccion)
        self.__piso = piso
        self.__balcon = balcon
        self.__nro_edificio = nro_edificio
        self.__cantidad_pisos = cantidad_pisos

    @property
    def piso(self):
        return self.__piso

    @piso.setter
    def piso(self, value):
        self.__piso = value

    @property
    def balcon(self):
        return self.__balcon

    @balcon.setter
    def balcon(self, value):
        self.__balcon = value

    @property
    def nro_edificio(self):
        return self.__nro_edificio

    @nro_edificio.setter
    def nro_edificio(self, value):
        self.__nro_edificio = value

    @property
    def cantidad_pisos(self):
        return self.__cantidad_pisos

    @cantidad_pisos.setter
    def cantidad_pisos(self, value):
        self.__cantidad_pisos = value

    # Para el inciso f Listado de datos de apartamentos de un edificio dado su dirección ordenado por el porciento de
    # terminación menor a mayor.   OK
    def comparar_direccion_edificio(self, direccion_dada):
        if self.direccion.reparto == direccion_dada.reparto and self.direccion.numero == int(direccion_dada.numero) and self.direccion.calle == direccion_dada.calle:
            return True
        else:
            return False


    def __str__(self):
        balcon = 'No'
        if self.balcon:
            balcon = 'Sí'
            # numero_de_identificacion, estado_de_terminacion, fecha_inicio, cantidad_metros_cuadrados,
            # cantidad_de_cuartos, direccion,  piso, balcon, nro_edificio, cantidad_pisos):
        return f"{Vivienda.__str__(self)}, " \
               f"{self.piso}, " \
               f"{balcon}, " \
               f"{self.nro_edificio}, " \
               f"{self.cantidad_pisos}"
