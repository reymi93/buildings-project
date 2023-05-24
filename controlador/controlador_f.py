from vista.funcion_f import FuncionListado
from modelo.repositorio import Repositorio
from modelo.direccion import Direccion

class ControladorFuncionF:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.repo = Repositorio()

    def iniciar(self):
        self.vista = FuncionListado(self)
        self.vista.show()

    def cargar_datos(self, lista):
        for viv_edi in lista:
            balcon = "No"
            if viv_edi.balcon:
                balcon = "Si"
            i = self.vista.tabla_viviendas.rowCount()
            self.vista.tabla_viviendas.insertRow(i)

            self.vista.agregar_vivienda(i, 0, str(viv_edi.numero_de_identificacion))
            self.vista.agregar_vivienda(i, 1, str(viv_edi.estado_de_terminacion))
            self.vista.agregar_vivienda(i, 2, str(viv_edi.fecha_inicio))
            self.vista.agregar_vivienda(i, 3, str(viv_edi.cantidad_metros_cuadrados))
            self.vista.agregar_vivienda(i, 4, str(viv_edi.cantidad_de_cuartos))
            self.vista.agregar_vivienda(i, 5, str(viv_edi.direccion))
            self.vista.agregar_vivienda(i, 6, str(viv_edi.piso))
            self.vista.agregar_vivienda(i, 7, balcon)
        self.vista.tabla_viviendas.resizeColumnsToContents()

    def mostrar_datos(self):
        try:
            self.vista.validar_controles()
            reparto = self.vista.valor_reparto
            calle = self.vista.valor_calle
            numero = self.vista.valor_de_numero
            direcc = Direccion(reparto, calle, numero)
            lista = self.repositorio.listado_de_datos(direcc)
            self.cargar_datos(lista)
            self.vista.restaurar_controles()

        except Exception as e:
            self.vista.mostrar_mensaje_de_error(e.args[0])