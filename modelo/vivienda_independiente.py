from modelo.vivienda import Vivienda


class Viviendaindependiente(Vivienda):
    def __init__(self, numero_de_identificacion, estado_de_terminacion, fecha_inicio, cantidad_metros_cuadrados, cantidad_de_cuartos, direccion, cochera, tipo_de_techo):
        Vivienda.__init__(self, numero_de_identificacion, estado_de_terminacion, fecha_inicio, cantidad_metros_cuadrados, cantidad_de_cuartos, direccion)
        self.__cochera = cochera
        self.__tipo_de_techo = tipo_de_techo



    @property
    def cochera(self):
        return self.__cochera

    @cochera.setter
    def cochera(self, value):
        self.__cochera = value

    @property
    def tipo_de_techo(self):
        return self.__tipo_de_techo

    @tipo_de_techo.setter
    def tipo_de_techo(self, value):
        self.__tipo_de_techo = value

    # Para el inciso e Porciento de viviendas que se están construyendo en un reparto dado con un tipo de cubierta
    # dada con garaje.      OK
    def es_techo(self, tipo_techo_dado):
        return self.tipo_de_techo == tipo_techo_dado

    def __str__(self):
        cochera = 'No'
        if self.cochera:
            cochera = 'Sí'
            # numero_de_identificacion, estado_de_terminacion, fecha_inicio, cantidad_metros_cuadrados,
            # cantidad_de_cuartos, direccion,  piso, balcon, nro_edificio, cantidad_pisos):
        return f"{Vivienda.__str__(self)}, " \
               f"{cochera}, " \
               f"{self.tipo_de_techo}"