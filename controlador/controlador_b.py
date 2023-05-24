from vista.funcion_b import FuncionDireccion
from modelo.repositorio import Repositorio


class ControladorFuncionB:
    def __init__(self, repositorio):
        self.__repositorio = repositorio
        self.__repo = Repositorio()

    def iniciar(self):
        self.__ventana = FuncionDireccion(self)
        self.__ventana.show()

    def mostrar_datos(self):
        direccion = self.__repositorio.direccion_viv_de_mayor_tiempo_con_menos_de_50()
        self.__ventana.valor_de_direccion = direccion.__str__()