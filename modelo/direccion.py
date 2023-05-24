class Direccion:
    def __init__(self, reparto, calle, numero):
        self.__reparto = reparto
        self.__calle = calle
        self.__numero = numero

    @property
    def reparto(self):
        return self.__reparto

    @reparto.setter
    def reparto(self, value):
        self.__reparto = value


    @property
    def calle(self):
        return self.__calle

    @calle.setter
    def calle(self, value):
        self.__calle = value


    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, value):
        self.__numero = value

    def __str__(self):
        return f"{self.reparto}, " \
               f"{self.calle}, " \
               f"#{self.numero}"