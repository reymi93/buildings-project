from modelo.direccion import Direccion
from modelo.viviendaen_edificio import Viviendaenedificio
from vista.vivienda_edificio import ViviendaEdificio
from PyQt5.QtCore import QDate
from datetime import date


class ControladorViviendaEdificio:
    def __init__(self, repo):
        self.vista = ViviendaEdificio(self)
        self.repositorio = repo


    def iniciar(self):
        self.cargar_datos()
        self.vista.setWindowTitle('Vivienda Edificios')
        self.vista.show()

    def cerrar(self):
        self.vista.close()

    def cargar_datos(self):
        try:
            self.vista.vaciar_tabla()
            for viv_edi in self.repositorio.lista_vivienda_edificio():
                balcon = 'No'
                if viv_edi.balcon:
                    balcon = 'Sí'
                i = self.vista.tabla_viviendas.rowCount()
                self.vista.tabla_viviendas.insertRow(i)
                self.vista.agregar_elemento_tabla(i, 0, str(viv_edi.numero_de_identificacion))
                self.vista.agregar_elemento_tabla(i, 1, str(viv_edi.estado_de_terminacion))
                self.vista.agregar_elemento_tabla(i, 2, str(viv_edi.fecha_inicio))
                self.vista.agregar_elemento_tabla(i, 3, str(viv_edi.cantidad_metros_cuadrados))
                self.vista.agregar_elemento_tabla(i, 4, str(viv_edi.cantidad_de_cuartos))
                self.vista.agregar_elemento_tabla(i, 5, str(viv_edi.direccion))
                self.vista.agregar_elemento_tabla(i, 6, str(viv_edi.piso))
                self.vista.agregar_elemento_tabla(i, 7, balcon)
                self.vista.agregar_elemento_tabla(i, 8, str(viv_edi.nro_edificio))
                self.vista.agregar_elemento_tabla(i, 9, str(viv_edi.cantidad_pisos))
            self.vista.tabla_viviendas.resizeColumnsToContents()
        except Exception as e:
            self.vista.mostrar_mensage_de_error(e.args[0])

    def insertar_viv_edif(self):
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
            piso = self.vista.piso
            balcon = self.vista.balcon
            edificio = self.vista.numero_edificio
            cant_pisos = self.vista.cantidad_pisos
            fecha = date(fecha_inicio.getDate()[0], fecha_inicio.getDate()[1],
                         fecha_inicio.getDate()[2])
            direccion = Direccion(reparto, calle, numero)
            viv = Viviendaenedificio(id, terminacion, fecha, metros,cuartos, direccion, piso, balcon, edificio, cant_pisos)
            self.repositorio.insertar_vivienda(viv)
            self.cargar_datos()
            self.vista.restablecer_controles()

        except Exception as e:
            self.vista.mostrar_error(e.args[0])

    def actualizar_viv_edif(self):
        try:
            ind = self.vista.tabla_viviendas.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para actualizarla.')
            ni_ant = self.vista.tabla_viviendas.item(ind, 0).text()
            self.vista.validar_controles()
            id = self.vista.numero_identificacion
            terminacion = self.vista.estado_terminacion
            fecha_inicio = self.vista.fecha
            fecha = date(fecha_inicio.getDate()[0], fecha_inicio.getDate()[1],
                         fecha_inicio.getDate()[2])
            metros = self.vista.cantidad_metro_cuadrados
            cuartos = self.vista.cantidad_cuartos
            reparto = self.vista.direccion_reparto
            calle = self.vista.direccion_calle
            numero = self.vista.direccion_numero
            piso = self.vista.piso
            balcon = self.vista.balcon
            edificio = self.vista.numero_edificio
            cant_pisos = self.vista.cantidad_pisos
            direccion = Direccion(reparto, calle, numero)
            viv = Viviendaenedificio(id, terminacion, fecha, metros,cuartos, direccion, piso, balcon, edificio, cant_pisos)
            self.repositorio.actualizar_vivienda(ni_ant, viv)
            self.cargar_datos()
            self.vista.restablecer_controles()
        except Exception as e:
            self.vista.mostrar_error(e.args[0])

    def eliminar_viv_edif(self):
        try:
            ind = self.vista.tabla_viviendas.currentRow()
            if ind == -1:
                raise Exception('Debe seleccionar una fila para eliminarla.')
            numero_de_identificacion = self.vista.tabla_viviendas.item(ind, 0).text()

            self.repositorio.eliminar_vivienda(numero_de_identificacion)
            self.cargar_datos()
            self.vista.restablecer_controles()
        except Exception as e:
            self.vista.mostrar_error(e.args[0])

    def llenar_formulario_x_tabla(self):
        ind = self.vista.tabla_viviendas.currentRow()
        if ind != -1:
            numero_identificacion = self.vista.tabla_viviendas.item(ind, 0).text()
            estado_de_terminacion = self.vista.tabla_viviendas.item(ind, 1).text()
            indice = self.repositorio.numero_de_identificacion_vivienda(numero_identificacion)
            vivienda = self.repositorio.lista_vivienda[indice]
            fecha_inicio = QDate(vivienda.fecha_inicio.year, vivienda.fecha_inicio.month,
                                 vivienda.fecha_inicio.day)
            cantidad_metros_cuadrados = self.vista.tabla_viviendas.item(ind, 3).text()
            cantidad_de_cuartos = self.vista.tabla_viviendas.item(ind, 4).text()
            piso = self.vista.tabla_viviendas.item(ind, 6).text()
            nro_edificio = self.vista.tabla_viviendas.item(ind, 8).text()
            cantidad_pisos = self.vista.tabla_viviendas.item(ind, 9).text()
            direccion = vivienda.direccion
            balcon = True
            if self.vista.tabla_viviendas.item(ind, 6).text() == 'No':
                balcon = False
            self.vista.numero_identificacion = numero_identificacion
            self.vista.estado_terminacion = estado_de_terminacion
            self.vista.fecha = fecha_inicio
            self.vista.cantidad_metro_cuadrados = cantidad_metros_cuadrados
            self.vista.cantidad_cuartos = cantidad_de_cuartos
            self.vista.piso = piso
            self.vista.numero_edificio = nro_edificio
            self.vista.cantidad_pisos = cantidad_pisos
            self.vista.direccion_reparto = direccion.reparto
            self.vista.direccion_calle = direccion.calle
            self.vista.direccion_numero = str(direccion.numero)
            self.vista.balcon = balcon