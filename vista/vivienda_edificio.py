from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import QDate
from PyQt5 import uic


class ViviendaEdificio(QDialog):
    def __init__(self, controlador):
        self.__controlador = controlador
        QDialog.__init__(self)
        uic.loadUi('vista/ui/vivienda_en_edificio.ui', self)

        self.btn_insertar.clicked.connect(self.__controlador.insertar_viv_edif)
        self.btn_modificar.clicked.connect(self.__controlador.actualizar_viv_edif)
        self.btn_eliminar.clicked.connect(self.__controlador.eliminar_viv_edif)
        self.btn_cerrar.clicked.connect(self.close)
        self.tabla_viviendas.itemClicked.connect(self.__controlador.llenar_formulario_x_tabla)

        self.tabla_viviendas.setColumnCount(10)
        self.tabla_viviendas.setHorizontalHeaderLabels(
            ['# Identificacion', 'Estado de Terminacion', 'Fecha de Inicio', '# Metros Cuadrados', '# Cuartos', 'Direccion', 'Piso', 'Balcon', '# Edificio', '# Pisos'])
        self.tabla_viviendas.resizeColumnsToContents()

        self.valor_fecha.setMaximumDate(QDate.currentDate())
        self.valor_fecha.setDate(QDate.currentDate())

    @property
    def numero_identificacion(self):
        return self.valor_numero_identificacion.text().strip()

    @numero_identificacion.setter
    def numero_identificacion(self, value):
        self.valor_numero_identificacion.setText(value)
    
    @property
    def estado_terminacion(self):
        return self.valor_estado_terminacion.text().strip()
    
    @estado_terminacion.setter
    def estado_terminacion(self, value):
        self.valor_estado_terminacion.setText(value)
    
    @property
    def fecha(self):
        return self.valor_fecha.date()
    
    @fecha.setter
    def fecha(self, date):
        self.valor_fecha.setDate(date)
    
    @property
    def cantidad_metro_cuadrados(self):
        return  self.valor_cantidad_metro_cuadrados.text().strip()
    
    @cantidad_metro_cuadrados.setter
    def cantidad_metro_cuadrados(self, value):
        self.valor_cantidad_metro_cuadrados.setText(value)

    @property
    def cantidad_cuartos(self):
        return self.valor_cantidad_cuartos.text().strip()

    @cantidad_cuartos.setter
    def cantidad_cuartos(self, value):
        self.valor_cantidad_cuartos.setText(value)
    
    @property
    def direccion_reparto(self):
        return self.valor_direccion_reparto.text().strip()
    
    @direccion_reparto.setter
    def direccion_reparto(self, value):
        self.valor_direccion_reparto.setText(value)
    
    @property
    def direccion_calle(self):
        return self.valor_direccion_calle.text().strip()
    
    @direccion_calle.setter
    def direccion_calle(self, value):
        self.valor_direccion_calle.setText(value)
    
    @property
    def direccion_numero(self):
        return self.valor_direccion_numero.text().strip()
    
    @direccion_numero.setter
    def direccion_numero(self, value):
        self.valor_direccion_numero.setText(value)
    
    @property
    def piso(self):
        return self.valor_piso.text().strip()
    
    @piso.setter
    def piso(self, value):
        self.valor_piso.setText(value)
    
    @property
    def balcon(self):
        return self.valor_balcon.isChecked()
    
    @balcon.setter
    def balcon(self, value):
        self.valor_balcon.setChecked(value)
    
    @property
    def numero_edificio(self):
        return self.valor_numero_edificio.text().strip()
    
    @numero_edificio.setter
    def numero_edificio(self, value):
        self.valor_numero_edificio.setText(value)
    
    @property
    def cantidad_pisos(self):
        return self.valor_cantidad_pisos.text().strip()
    
    @cantidad_pisos.setter
    def cantidad_pisos(self, value):
        self.valor_cantidad_pisos.setText(value)

    def validar_controles(self):
        msg = 'El atributo {} es obligatorio.'
        ni = self.numero_identificacion
        et = self.estado_terminacion
        cm = self.cantidad_metro_cuadrados
        cc = self.cantidad_cuartos
        dr = self.direccion_reparto
        dc = self.direccion_calle
        dn = self.direccion_numero
        ps = self.piso
        ne = self.numero_edificio
        cp = self.cantidad_pisos
        if len(ni) == 0:
            raise Exception(msg.format('numero de identificacion'))
        if not ni.isdigit():
            raise Exception('El numero de identificacion sólo puede contener números.')
        if len(self.estado_terminacion) == 0:
            raise Exception(msg.format('estado de terminacion'))
        if not et.isdigit():
            raise Exception('El estado de terminacion sólo puede contener números.')
        if len(self.cantidad_metro_cuadrados) == 0:
            raise Exception(msg.format('estado de terminacion'))
        if not cm.isdigit():
            raise Exception('Los metros cuadrados tienen que ser numeros')
        if len(self.cantidad_cuartos) == 0:
            raise Exception(msg.format('cantidad de cuartos'))
        if not cc.isdigit():
            raise Exception('La cantidad de cuartos tienen que ser numeros')
        if len(self.direccion_reparto) == 0:
            raise Exception(msg.format('reparto'))
        if len(self.direccion_calle) == 0:
            raise Exception(msg.format('calle'))
        if len(self.direccion_numero) == 0:
            raise Exception(msg.format('numero'))
        if not dc.isalpha():
            raise Exception('La calle solo puede contener letras')
        if not dr.isalpha():
            raise Exception('El reparto solo puede contener letras')
        if not dn.isdigit():
            raise Exception('El numero de la direccion solo puede contener digitos')
        if len(self.piso) == 0:
            raise Exception(msg.format('piso'))
        if not ps.isdigit():
            raise Exception('El piso puede contener digitos')
        if len(self.numero_edificio) == 0:
            raise Exception(msg.format('numero del edificio'))
        if not ne.isdigit():
            raise Exception('EL numero del edificio puede contener digitos')
        if len(self.cantidad_pisos) == 0:
            raise Exception(msg.format('cantidad de pisos'))
        if not cp.isdigit():
            raise Exception('La cantidad puede contener digitos')

    def restablecer_controles(self):
        self.numero_identificacion = ''
        self.estado_terminacion = ''
        self.fecha = QDate.currentDate()
        self.cantidad_metro_cuadrados = ''
        self.cantidad_cuartos = ''
        self.direccion_reparto = ''
        self.direccion_calle = ''
        self.direccion_numero = ''
        self.piso = ''
        self.balcon = False
        self.numero_edificio = ''
        self.cantidad_pisos = ''

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error', msg)

    def vaciar_tabla(self):
        while self.tabla_viviendas.rowCount() > 0:
            self.tabla_viviendas.removeRow(0)

    def agregar_elemento_tabla(self, fila, columna, texto):
        self.tabla_viviendas.setItem(fila, columna, QTableWidgetItem(texto))
