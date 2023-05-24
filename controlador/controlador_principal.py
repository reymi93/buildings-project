import sys
from PyQt5.QtWidgets import QApplication
from vista.ventana_principal import VentanaPrincipal
from controlador.controlador_ventana_edificio import ControladorViviendaEdificio
from controlador.controlador_ventana_independiente import ControladorVentanaIndependiente
from modelo.direccion import Direccion
from modelo.repositorio import *
from controlador.controlador_b import ControladorFuncionB
from controlador.controlador_c import ControladorFuncionC
from controlador.controlador_d import ControladorFuncionD
from controlador.controlador_e import ControladorFuncionE
from controlador.controlador_f import ControladorFuncionF


class ControladorPrincipal:
    def __init__(self):
        self.__repositorio = Repositorio()

        fech1 = date(2020, 3, 4)
        fech2 = date(2010, 10, 11)
        fech3 = date(2016, 4, 2)
        fech4 = date(2014, 11, 2)

        fecha = date(2012, 10, 1)
        fechb = date(2014, 9, 1)
        fechc = date(2015, 8, 2)
        fechd = date(2013, 7, 3)
        feche = date(2014, 12, 4)
        fechf = date(2015, 10, 2)
        fechg = date(1900, 5, 4)

        direccion1 = Direccion('Florat', 'Calle 7', 24)
        direccion2 = Direccion('Vista Hermosa', 'Calle 5', 16)
        direccion3 = Direccion('Montecarlos', 'Resplandor', 22)
        direccion4 = Direccion('Centro', 'Republica', 286)

        direcciona = Direccion('Jardin', 'Desengaño', 12)
        direccionb = Direccion('Vigia', 'Capdevila', 23)
        direccionc = Direccion('Timbalito', 'Agramonte', 35)
        direcciond = Direccion('Centro', 'Cristo', 3)
        direccione = Direccion('Vigia', 'Capdevila', 32)
        direccionf = Direccion('Zambrana', 'Avenida Camaguey', 7)
        direcciong = Direccion('Vigia', 'Capdevila', 84)

        # numero_de_identificacion, estado_de_terminacion, fecha_inicio, cantidad_metros_cuadrados,
        # cantidad_de_cuartos, direccion, piso, balcon, nro_edificio, cantidad_pisos
        vivienda1 = Viviendaenedificio(14, 23, fech1, 16, 3, direccion1, 2, False, 3, 3)
        vivienda2 = Viviendaenedificio(12, 42, fech2, 10, 3, direccion1, 2, True, 3, 3)
        vivienda5 = Viviendaenedificio(15, 2, fech1, 16, 3, direccion1, 2, False, 3, 3)
        vivienda6 = Viviendaenedificio(16, 51, fech2, 10, 3, direccion1, 2, True, 3, 3)
        vivienda3 = Viviendaenedificio(8, 10, fech3, 20, 2, direccion3, 3, True, 1, 1)
        vivienda4 = Viviendaenedificio(9, 3, fech4, 12, 1, direccion4, 1, False, 2, 2)

        # numero_de_identificacion, estado_de_terminacion, fecha_inicio, cantidad_metros_cuadrados,
        # cantidad_de_cuartos, direccion, cochera, tipo_de_techo
        viviendaa = Viviendaindependiente(80, 59, fecha, 101, 22, direcciona, True, 'teja', )
        viviendab = Viviendaindependiente(89, 60, fechb, 20, 12, direccionb, False, 'placa', )
        viviendac = Viviendaindependiente(102, 70, fechc, 20, 1, direccionc, False, "teja")
        viviendad = Viviendaindependiente(103, 10, fechd, 18, 1, direcciond, True, "")
        viviendae = Viviendaindependiente(104, 30, feche, 30, 2, direccione, True, "placa")
        viviendaf = Viviendaindependiente(105, 20, fechf, 40, 3, direccionf, False, "teja")
        viviendag = Viviendaindependiente(106, 42, fechg, 50, 4, direcciong, True, "placa")

        self.__repositorio.lista_vivienda.append(vivienda1)
        self.__repositorio.lista_vivienda.append(vivienda2)
        self.__repositorio.lista_vivienda.append(vivienda3)
        self.__repositorio.lista_vivienda.append(vivienda4)
        self.__repositorio.lista_vivienda.append(vivienda5)
        self.__repositorio.lista_vivienda.append(vivienda6)

        self.__repositorio.lista_vivienda.append(viviendaa)
        self.__repositorio.lista_vivienda.append(viviendab)
        self.__repositorio.lista_vivienda.append(viviendac)
        self.__repositorio.lista_vivienda.append(viviendad)
        self.__repositorio.lista_vivienda.append(viviendae)
        self.__repositorio.lista_vivienda.append(viviendaf)
        self.__repositorio.lista_vivienda.append(viviendag)

    def iniciar(self):
        self.__app = QApplication(sys.argv)
        self.__window_principal = VentanaPrincipal(self)
        self.__window_principal.iniciar()
        self.__app.exec_()

    def cerrar(self):
        self.__window_principal.cerrar()

    def action_vivienda_edificio(self):
        p = ControladorViviendaEdificio(self.__repositorio)
        p.iniciar()

    def action_vivienda_independiente(self):
        p = ControladorVentanaIndependiente(self.__repositorio)
        p.iniciar()

    def funcionalidad_b(self):
        p = ControladorFuncionB(self.__repositorio)
        p.iniciar()

    def funcionalidad_c(self):
        p = ControladorFuncionC(self.__repositorio)
        p.iniciar()

    def funcionalidad_d(self):
        p = ControladorFuncionD(self.__repositorio)
        p.iniciar()

    def funcionalidad_e(self):
        p = ControladorFuncionE(self.__repositorio)
        p.iniciar()

    def funcionalidad_f(self):
        p = ControladorFuncionF(self.__repositorio)
        p.iniciar()
