from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic


class FuncionPorciento(QDialog):
    def __init__(self, controlador):
        self.__controlador = controlador
        QDialog.__init__(self)
        uic.loadUi("vista/ui/e.ui", self)

        self.boton_calcular.clicked.connect(self.__controlador.porciento_de_viviendas)
        self.boton_cerrar.clicked.connect(self.close)

    @property
    def valor_tipo_de_techo(self):
        return self.tipo_de_techo.currentText()

    @valor_tipo_de_techo.setter
    def valor_tipo_de_techo(self, value):
        self.tipo_de_techo.setCurrentText(value)
    
    @property
    def valor_de_reparto(self):
        return self.reparto.text().strip()
    
    @valor_de_reparto.setter
    def valor_de_reparto(self, value):
        self.reparto.setText(value)
    
    @property
    def valor_de_porciento(self):
        return self.porciento.text().strip()
    
    @valor_de_porciento.setter
    def valor_de_porciento(self, value):
        self.porciento.setText(value)

    def validar_controles(self):
        rep_direc = self.valor_de_reparto.split()
        for i in rep_direc:
            if not i.isalpha():
                raise Exception("El campo Reparto solo puede contener letras del alphabeto inglés.")
    
    def restaurar_valores(self):
        self.valor_tipo_de_techo = "placa"
        self.valor_de_reparto = ""

    def restaurar_porciento(self):
        self.valor_de_porciento = ""

    def mostrar_mensaje_de_error(self, mensage):
        QMessageBox.critical(self, "Error", mensage)

    def mostrar_mensaje(self, titulo, mensage):
        QMessageBox.information(self, titulo, mensage)