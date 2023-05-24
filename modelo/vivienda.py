class Vivienda:
    def __init__(self, numero_de_identificacion, estado_de_terminacion, fecha_inicio, cantidad_metros_cuadrados, cantidad_de_cuartos, direccion):
        self.__numero_de_identificacion = numero_de_identificacion
        self.__estado_de_terminacion = estado_de_terminacion
        self.__fecha_inicio = fecha_inicio
        self.__cantidad_metros_cuadrados = cantidad_metros_cuadrados
        self.__cantidad_de_cuartos = cantidad_de_cuartos
        self.__direccion = direccion


    @property
    def numero_de_identificacion(self):
        return self.__numero_de_identificacion

    @numero_de_identificacion.setter
    def numero_de_identificacion(self, value):
        self.__numero_de_identificacion = value



    @property
    def estado_de_terminacion(self):
        return self.__estado_de_terminacion

    @estado_de_terminacion.setter
    def estado_de_terminacion(self, value):
        self.__estado_de_terminacion = value



    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value):
        self.__fecha_inicio = value



    @property
    def cantidad_metros_cuadrados(self):
        return self.__cantidad_metros_cuadrados

    @cantidad_metros_cuadrados.setter
    def cantidad_metros_cuadrados(self, value):
        self.__cantidad_metros_cuadrados = value



    @property
    def cantidad_de_cuartos(self):
        return self.__cantidad_de_cuartos

    @cantidad_de_cuartos.setter
    def cantidad_de_cuartos(self, value):
        self.cantidad_de_cuartos = value

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, value):
        self.__direccion = value

    #def direccion(self):
    #    return str(self.direccion.reparto) + "calle" + str(self.direccion.calle) + "numero" + (self.direccion.numero)

    def es_reparto(self, reparto_dado):
        return self.direccion.reparto == reparto_dado

    def es_numero_de_identificacion(self, numero_de_identificacion):
        return int(self.numero_de_identificacion) == int(numero_de_identificacion)


    def __str__(self):
        return f"{self.numero_de_identificacion}, " \
               f"{self.estado_de_terminacion}, " \
               f"{self.fecha_inicio}, " \
               f"{self.cantidad_metros_cuadrados}, " \
               f"{self.cantidad_de_cuartos}, " \
               f"{self.direccion}"

    # inciso b
    def comparar_fechas(self, fecha):
        return self.fecha_inicio < fecha

    def comparar_estados_en_menor(self, porciento_estado):
        return int(self.estado_de_terminacion) < porciento_estado

    # inciso c
    def es_direccion(self, direccion_dada):
        if self.direccion.reparto == direccion_dada.reparto and self.direccion.numero == direccion_dada.numero and self.direccion.calle == direccion_dada.calle:
            return True
        else:
            return False

    # inciso d
    def comparar_estados_en_igual(self, porciento):
        return self.estado_de_terminacion == porciento