from modelo.direccion import Direccion
from modelo.vivienda_independiente import Viviendaindependiente
from vista.vivienda_independiente import ViviendaIndependiente
from PyQt5.QtCore import QDate
from datetime import date


class ControladorVentanaIndependiente:
    def __init__(self, repo):
        self.repositorio = repo
        self.vista = ViviendaIndependiente(self)

    def iniciar(self):
        self.cargar_datos()
        self.vista.show()
        self.vista.setWindowTitle('Viviendas Independientes')

    def cerrar(self):
        self.vista.close()

    def cargar_datos(self):
        try:
            self.vista.vaciar_tabla()
            for viv_ide in self.repositorio.lista_vivienda_independiente():
                cochera = 'No'
                if viv_ide.cochera:
                    cochera = 'Sí'
                i = self.vista.tabla_viviendas_ind.rowCount()
                self.vista.tabla_viviendas_ind.insertRow(i)
                self.vista.agregar_elemento_tabla(i, 0, str(viv_ide.numero_de_identificacion))
                self.vista.agregar_elemento_tabla(i, 1, str(viv_ide.estado_de_terminacion))
                self.vista.agregar_elemento_tabla(i, 2, str(viv_ide.fecha_inicio))
                self.vista.agregar_elemento_tabla(i, 3, str(viv_ide.cantidad_metros_cuadrados))
                self.vista.agregar_elemento_tabla(i, 4, str(viv_ide.cantidad_de_cuartos))
                self.vista.agregar_elemento_tabla(i, 5, str(viv_ide.direccion))
                self.vista.agregar_elemento_tabla(i, 6, cochera)
                self.vista.agregar_elemento_tabla(i, 7, str(viv_ide.tipo_de_techo))
            self.vista.tabla_viviendas_ind.resizeColumnsToContents()
        except Exception as e:
            self.vista.mostrar_error(e.args[0])

    def insertar_viv_ind(self):
        try:
            self.vista.validar_controles()
            id = self.vista.numero_identificacion
            terminacion = self.vista.estado_terminacion
            fecha_inicio = self.vista.fecha
            metros = self.vista.cantidad_metro_cuadrados
            cuartos = self.vista.cantidad_cuartos
            reparto = self.vista.direccion_reparto
            calle = self.vista.direccion_calle
            numero = self.vista.direccion_numero
            cochera = self.vista.cochera
            tipo_techo = self.vista.tipo_de_techo
            fecha = date(fecha_inicio.getDate()[0], fecha_inicio.getDate()[1],
                         fecha_inicio.getDate()[2])
            direccion = Direccion(reparto, calle, numero)
            viv = Viviendaindependiente(id, terminacion, fecha, metros, cuartos, direccion, cochera, tipo_techo)
            self.repositorio.insertar_vivienda(viv)
            self.cargar_datos()
            self.vista.restablecer_controles()

        except Exception as e:
            self.vista.mostrar_error(e.args[0])

    def actualizar_viv_ind(self):
        try:
            ind = self.vista.tabla_viviendas_ind.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para actualizarla.')
            ni_ant = self.vista.tabla_viviendas_ind.item(ind, 0).text()
            self.vista.validar_controles()
            id = self.vista.numero_identificacion
            terminacion = self.vista.estado_terminacion
            fecha_inicio = self.vista.fecha
            metros = self.vista.cantidad_metro_cuadrados
            cuartos = self.vista.cantidad_cuartos
            reparto = self.vista.direccion_reparto
            calle = self.vista.direccion_calle
            numero = self.vista.direccion_numero
            cochera = self.vista.cochera
            tipo_techo = self.vista.tipo_de_techo
            fecha = date(fecha_inicio.getDate()[0], fecha_inicio.getDate()[1],
                         fecha_inicio.getDate()[2])
            direccion = Direccion(reparto, calle, numero)
            viv = Viviendaindependiente(id, terminacion, fecha, metros, cuartos, direccion, cochera, tipo_techo)
            self.repositorio.actualizar_vivienda(ni_ant, viv)
            self.cargar_datos()
            self.vista.restablecer_controles()
        except Exception as e:
            self.vista.mostrar_error(e.args[0])

    def eliminar_viv_ind(self):
        try:
            ind = self.vista.tabla_viviendas_ind.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para eliminarla.')
            numero_de_identificacion = self.vista.tabla_viviendas_ind.item(ind, 0).text()

            self.repositorio.eliminar_vivienda(numero_de_identificacion)
            self.cargar_datos()
            self.vista.restablecer_controles()
        except Exception as e:
            self.vista.mostrar_error(e.args[0])

    def llenar_formulario_x_tabla(self):
        ind = self.vista.tabla_viviendas_ind.currentRow()
        if ind != -1:
            numero_identificacion = self.vista.tabla_viviendas_ind.item(ind, 0).text()
            estado_de_terminacion = self.vista.tabla_viviendas_ind.item(ind, 1).text()
            indice = self.repositorio.numero_de_identificacion_vivienda(numero_identificacion)
            vivienda = self.repositorio.lista_vivienda[indice]
            fecha_inicio = QDate(vivienda.fecha_inicio.year, vivienda.fecha_inicio.month,
                                 vivienda.fecha_inicio.day)
            cantidad_metros_cuadrados = self.vista.tabla_viviendas_ind.item(ind, 3).text()
            cantidad_de_cuartos = self.vista.tabla_viviendas_ind.item(ind, 4).text()
            tipo_de_techo = self.vista.tabla_viviendas_ind.item(ind, 7).text()
            direccion = vivienda.direccion
            cochera = True
            if self.vista.tabla_viviendas_ind.item(ind, 6).text() == 'No':
                cochera = False
            self.vista.numero_identificacion = numero_identificacion
            self.vista.estado_terminacion = estado_de_terminacion
            self.vista.fecha = fecha_inicio
            self.vista.cantidad_metro_cuadrados = cantidad_metros_cuadrados
            self.vista.cantidad_cuartos = cantidad_de_cuartos
            self.vista.tipo_de_techo = tipo_de_techo
            self.vista.direccion_reparto = direccion.reparto
            self.vista.direccion_calle = direccion.calle
            self.vista.direccion_numero = str(direccion.numero)
            self.vista.cochera = cochera
