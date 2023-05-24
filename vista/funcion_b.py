from PyQt5.QtWidgets import QDialog
from PyQt5 import uic


class FuncionDireccion(QDialog):
    def __init__(self, controlador):
        self.__controlador = controlador
        QDialog.__init__(self)
        uic.loadUi("vista/ui/b.ui", self)

        self.boton_mostrar.clicked.connect(self.__controlador.mostrar_datos)
        self.boton_cerrar.clicked.connect(self.close)

    @property
    def valor_de_direccion(self):
        return self.direccion_de_la_vivienda.text().strip()

    @valor_de_direccion.setter
    def valor_de_direccion(self, value):
        self.direccion_de_la_vivienda.setText(value)