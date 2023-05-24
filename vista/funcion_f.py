from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5 import uic


class FuncionListado(QDialog):
    def __init__(self, controlador):
        self.__controlador = controlador
        QDialog.__init__(self)
        uic.loadUi("vista/ui/f.ui", self)

        self.boton_mostrar.clicked.connect(self.__controlador.mostrar_datos)
        self.boton_cerrar.clicked.connect(self.close)

        self.tabla_viviendas.setColumnCount(8)
        self.tabla_viviendas.setHorizontalHeaderLabels(["Número de identificación", "Estado de terminación", "Inicio de construcción",
                                                   "Metros cuadrados", "Cantidad de cuartos", "Dirección", "Tipo de piso", "Tiene balcón"])
        self.tabla_viviendas.resizeColumnsToContents()
    
    @property
    def valor_reparto(self):
        return self.reparto_del_edificio.text().strip()
    
    @valor_reparto.setter
    def valor_reparto(self, value):
        self.reparto_del_edificio.setText(value)

    @property
    def valor_calle(self):
        return self.calle_del_edificio.text().strip()

    @valor_calle.setter
    def valor_calle(self, value):
        self.calle_del_edificio.setText(value)

    @property
    def valor_de_numero(self):
        return self.numero_del_edificio.text().strip()

    @valor_de_numero.setter
    def valor_de_numero(self, value):
        self.numero_del_edificio.setText(value)

    def restaurar_controles(self):
        self.valor_reparto = ""
        self.valor_calle = ""
        self.valor_de_numero = ""

    def validar_controles(self):
        mensage = "El campo {} es necesario."
        if len(self.valor_calle) == 0:
            raise Exception(mensage.format("Calle"))
        if len(self.valor_de_numero) == 0:
            raise Exception(mensage.format("Número"))
        if not self.valor_de_numero.isnumeric():
            raise Exception("El campo Número del edificio solo puede contener números.")

        rep_direc = self.valor_reparto.split()
        call_direc = self.valor_calle.split()
        for i in rep_direc:
            if not i.isalpha():
                raise Exception("El campo Reparto solo puede contener letras del alphabeto inglés.")
        for i in call_direc:
            if not i.isalnum():
                raise Exception("El campo Calle solo puede contener números, letras del alfabeto inglés o ambas.")

    def mostrar_mensaje_de_error(self, mensage):
        QMessageBox.critical(self, "Error", mensage)

    def agregar_vivienda(self, fila, columna, texto):
        self.tabla_viviendas.setItem(fila, columna, QTableWidgetItem(texto))