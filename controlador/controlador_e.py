from vista.funcion_e import FuncionPorciento
from modelo.repositorio import Repositorio


class ControladorFuncionE:
    def __init__(self, controlador):
        self.repositorio = controlador
        self.repo = Repositorio()

    def iniciar(self):
        self.vista = FuncionPorciento(self)
        self.vista.show()

    def porciento_de_viviendas(self):
        try:
            self.vista.validar_controles()
            techo = self.vista.valor_tipo_de_techo
            reparto = self.vista.valor_de_reparto
            if self.repositorio.indice_de_vivienda_por_reparto(reparto) is None:
                raise Exception("No existe este reparto en las direcciones de viviendas de la empresa.")
            porciento = self.repositorio.porciento_de_viviendas(techo, reparto)
            self.vista.valor_de_porciento = str(porciento) + "%"
            self.vista.restaurar_valores()

        except ZeroDivisionError:
            self.vista.mostrar_mensaje("Mensaje", "Ninguna vivienda con cochera en este reparto posee este tipo de techo.")

        except Exception as e:
            self.vista.mostrar_mensaje_de_error(e.args[0])
