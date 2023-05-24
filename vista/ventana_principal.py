from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QResizeEvent
from PyQt5.QtCore import Qt


class VentanaPrincipal(QMainWindow):
    def __init__(self, controlador):
        QMainWindow.__init__(self)
        uic.loadUi("vista/ui/ventana.ui", self)
        self.__controlador = controlador

        self.actionVivienda_Independiente.triggered.connect(self.__controlador.action_vivienda_independiente)
        self.actionVivienda_en_edificio.triggered.connect(self.__controlador.action_vivienda_edificio)
        self.actionb.triggered.connect(self.__controlador.funcionalidad_b)
        self.actionc.triggered.connect(self.__controlador.funcionalidad_c)
        self.actiond.triggered.connect(self.__controlador.funcionalidad_d)
        self.actione.triggered.connect(self.__controlador.funcionalidad_e)
        self.actionf.triggered.connect(self.__controlador.funcionalidad_f)

    def iniciar(self):
        self.show()

    def cerrar(self):
        self.close()

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def resizeEvent(self, a0: QResizeEvent):
        background = QPixmap('vista/imgs/cayo-cruz.jpg')
        background = background.scaled(self.size(), Qt.IgnoreAspectRatio)  # KeepAspectRatio, KeepAspectRatioByExpanding
        pal = self.palette()
        pal.setBrush(QPalette.Background, QBrush(background))
        self.setPalette(pal)
