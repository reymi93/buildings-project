from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic

class FuncionMaximoArea(QDialog):
    def __init__(self, controlador):
        self.__controlador = controlador
        QDialog.__init__(self)
        uic.loadUi("vista/ui/c.ui", self)

        self.boton_calcular.clicked.connect(self.__controlador.maxima_area)
        self.boton_cerrar.clicked.connect(self.close)

    @property
    def valor_del_reparto_del_edificio(self):
        return self.reparto_del_edificio.text().strip()

    @valor_del_reparto_del_edificio.setter
    def valor_del_reparto_del_edificio(self, value):
        self.reparto_del_edificio.setText(value)

    @property
    def valor_de_calle_del_edificio(self):
        return self.calle_del_edificio.text().strip()

    @valor_de_calle_del_edificio.setter
    def valor_de_calle_del_edificio(self, value):
        self.calle_del_edificio.setText(value)

    @property
    def valor_del_numero_del_edificio(self):
        return self.numero_del_edificio.text().strip()

    @valor_del_numero_del_edificio.setter
    def valor_del_numero_del_edificio(self, value):
        self.numero_del_edificio.setText(value)

    @property
    def valor_del_piso(self):
        return self.piso_del_edificio.text().strip()

    @valor_del_piso.setter
    def valor_del_piso(self, value):
        self.piso_del_edificio.setText(value)

    @property
    def valor_del_area_maxima(self):
        return self.area_maxima.text()

    @valor_del_area_maxima.setter
    def valor_del_area_maxima(self, value):
        self.area_maxima.setText(value)

    def validar_controles(self):
        mensage = "El campo {} es necesario."
        if len(self.valor_de_calle_del_edificio) == 0:
            raise Exception(mensage.format("Calle del edificio"))
        if len(self.valor_del_numero_del_edificio) == 0:
            raise Exception(mensage.format("Número del edificio"))
        if len(self.valor_del_piso) == 0:
            raise Exception(mensage.format("Piso"))

        mensage2 = "El campo {} solo puede contener números"
        if not self.valor_del_numero_del_edificio.isdigit():
            raise Exception(mensage2.format("Número del edificio"))
        if not self.valor_del_piso.isdigit():
            raise Exception(mensage2.format("Piso"))

        rep_direc = self.valor_del_reparto_del_edificio.split()
        call_direc = self.valor_de_calle_del_edificio.split()
        for i in rep_direc:
            if not i.isalpha():
                raise Exception("El campo Reparto solo puede contener letras del alphabeto inglés.")
        for i in call_direc:
            if not i.isalnum():
                raise Exception("El campo Calle solo puede contener números, letras del alfabeto inglés o ambas.")

    def restaurar_controles(self):
        self.valor_del_reparto_del_edificio = ""
        self.valor_de_calle_del_edificio = ""
        self.valor_del_numero_del_edificio = ""
        self.valor_del_piso = ""

    def mostrar_mensaje_de_error(self, mensage):
        QMessageBox.critical(self, "Error", mensage)