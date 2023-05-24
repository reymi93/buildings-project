from vista.funcion_d import FuncionDatosVivienda
from modelo.repositorio import Repositorio


class ControladorFuncionD:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.repo = Repositorio()

    def iniciar(self):
        self.vista = FuncionDatosVivienda(self)
        self.vista.show()

    def mostrar_datos(self):
        try:
            techo = self.vista.valor_tipo_de_techo
            datos = self.repositorio.vivienda_sin_garaje_mas_atrasada(techo)
            if datos == None:
                raise Exception("En el listado no existe una vivienda sin cochera con este tipo de techo.")
            self.vista.tabla_de_datos.insertRow(0)

            self.vista.agregar_datos_a_la_tabla(0, 0, str(datos.numero_de_identificacion))
            self.vista.agregar_datos_a_la_tabla(0, 1, str(datos.estado_de_terminacion))
            self.vista.agregar_datos_a_la_tabla(0, 2, str(datos.fecha_inicio))
            self.vista.agregar_datos_a_la_tabla(0, 3, str(datos.cantidad_metros_cuadrados))
            self.vista.agregar_datos_a_la_tabla(0, 4, str(datos.cantidad_de_cuartos))
            self.vista.agregar_datos_a_la_tabla(0, 5, str(datos.direccion))
            self.vista.agregar_datos_a_la_tabla(0, 6, "No")
            self.vista.agregar_datos_a_la_tabla(0, 7, str(datos.tipo_de_techo))
            self.vista.tabla_de_datos.resizeColumnsToContents()
            self.vista.restaurar_controles()

        except Exception as e:
            self.vista.mostrar_mensaje_de_error(e.args[0])