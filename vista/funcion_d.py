from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5 import uic


class FuncionDatosVivienda(QDialog):
    def __init__(self, controlador):
        self.__controlador = controlador
        QDialog.__init__(self)
        uic.loadUi("vista/ui/d.ui", self)

        self.boton_mostrar.clicked.connect(self.__controlador.mostrar_datos)
        self.boton_cerrar.clicked.connect(self.close)

        self.tabla_de_datos.setColumnCount(8)
        self.tabla_de_datos.setHorizontalHeaderLabels(
            ["Número de identificación", "Estado de terminación", "Inicio de construcción", "Metros cuadrados",
             "Cantidad de cuartos",
             "Dirección", "Tiene garaje", "Tipo de techo"])
        self.tabla_de_datos.resizeColumnsToContents()

    @property
    def valor_tipo_de_techo(self):
        return self.tipo_de_techo.currentText()

    @valor_tipo_de_techo.setter
    def valor_tipo_de_techo(self, value):
        self.tipo_de_techo.setCurrentText(value)

    def restaurar_controles(self):
        self.valor_tipo_de_techo = "placa"

    def mostrar_mensaje_de_error(self, mensage):
        QMessageBox.critical(self, "Error", mensage)

    def agregar_datos_a_la_tabla(self, fila, columna, texto):
        self.tabla_de_datos.setItem(fila, columna, QTableWidgetItem(texto))
