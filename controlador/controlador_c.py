from vista.funcion_c import FuncionMaximoArea
from modelo.repositorio import Repositorio
from modelo.direccion import Direccion


class ControladorFuncionC:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.repo = Repositorio()

    def iniciar(self):
        self.vista = FuncionMaximoArea(self)
        self.vista.show()

    def maxima_area(self):
        try:
            self.vista.validar_controles()
            reparto = str(self.vista.valor_del_reparto_del_edificio)
            calle = str(self.vista.valor_de_calle_del_edificio)
            numero = int(self.vista.valor_del_numero_del_edificio)
            piso = int(self.vista.valor_del_piso)
            direccion = Direccion(reparto, calle, numero)
            if self.repositorio.indice_de_vivienda_por_direccion(direccion) is None:
                raise Exception("En la dirección dada no se encuentra ningún apartamento.")
            area_maxima = self.repositorio.area_maxima(direccion, piso)
            self.vista.valor_del_area_maxima = str(area_maxima)
            self.vista.restaurar_controles()

        except Exception as e:
            self.vista.mostrar_mensaje_de_error(e.args[0])