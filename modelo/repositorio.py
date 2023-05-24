from modelo.viviendaen_edificio import Viviendaenedificio
from modelo.vivienda_independiente import Viviendaindependiente
from datetime import date
from operator import attrgetter


class Repositorio:
    def __init__(self):
        self.__lista_vivienda = []

    @property
    def lista_vivienda(self):
        return self.__lista_vivienda

    @lista_vivienda.setter
    def lista_vivienda(self, value):
        self.__lista_vivienda = value

    def numero_de_identificacion_vivienda(self, numero_de_identificacion):
        for i in range(len(self.lista_vivienda)):
            if self.lista_vivienda[i].es_numero_de_identificacion(int(numero_de_identificacion)):
                return i

    def indice_de_vivienda_por_direccion(self, direccion_dada):
        for i in range(len(self.lista_vivienda)):
            # print(self.lista_vivienda[i])
            if self.lista_vivienda[i].es_direccion(direccion_dada):
                # print(self.lista_vivienda[i].es_direccion(direccion_dada))
                return i

    def insertar_vivienda(self, viv):
        if self.numero_de_identificacion_vivienda(viv.numero_de_identificacion) != None:
            raise Exception('El ID de la vivienda ya existe')
        self.lista_vivienda.append(viv)

    def actualizar_vivienda(self, ni_ant, viv):
        ind_ant = self.numero_de_identificacion_vivienda(ni_ant)
        if ind_ant == None:
            raise Exception('La vivienda no existe')
        ind_nue1 = self.numero_de_identificacion_vivienda(viv.numero_de_identificacion)
        if (ind_nue1 != None and ind_nue1 != ind_ant):
            raise Exception('La vivienda existe en el controlador')
        self.lista_vivienda[ind_ant] = viv

    def eliminar_vivienda(self, numero_de_identificacion):
        ind = self.numero_de_identificacion_vivienda(numero_de_identificacion)
        if ind == None:
            raise Exception('La vivienda no existe')
        self.lista_vivienda.remove(self.lista_vivienda[ind])

    def lista_vivienda_edificio(self):
        vivs_edi = []
        for viv in self.lista_vivienda:
            if isinstance(viv, Viviendaenedificio):
                vivs_edi.append(viv)
        return vivs_edi

    def lista_vivienda_independiente(self):
        vivs_ide = []
        for viv in self.lista_vivienda:
            if isinstance(viv, Viviendaindependiente):
                vivs_ide.append(viv)
        return vivs_ide

    # inc b Vivienda que más tiempo lleva en construcción y no pasa del 50% de construcción.
    def direccion_viv_de_mayor_tiempo_con_menos_de_50(self):
        listado = []
        direccion_de_vivienda = None
        fecha_menor = date(3000, 12, 12)
        for vivienda in self.lista_vivienda:
            if vivienda.comparar_estados_en_menor(50):
                listado.append(vivienda)
                if fecha_menor == None or vivienda.comparar_fechas(fecha_menor):
                    fecha_menor = vivienda.fecha_inicio
                    direccion_de_vivienda = vivienda.direccion
        return direccion_de_vivienda

    # inc c Tamaño máximo de área de los apartamentos de un piso dado que se construyen en un edificio dado su
    # dirección.        OK
    def area_maxima(self, direccion_dada, piso):
        area_max = 0
        for vivienda in self.lista_vivienda_edificio():
            if vivienda.es_direccion(direccion_dada) and vivienda.piso == piso:
                area_max += vivienda.cantidad_metros_cuadrados
        return area_max

    # inc d Datos de la vivienda independiente sin garaje con un tipo de cubierta dada más atrasada a su terminación.
    # OK
    def vivienda_sin_garaje_mas_atrasada(self, tipo_techo_dado):
        listado = []
        datos = None
        menor_porciento = 100
        fecha = None
        for vivienda in self.lista_vivienda_independiente():
            if vivienda.cochera == False and vivienda.es_techo(tipo_techo_dado):
                listado.append(vivienda)
        for viv in listado:
            if viv.comparar_estados_en_menor(menor_porciento):
                menor_porciento = viv.estado_de_terminacion
                fecha = viv.fecha_inicio
                datos = viv
            elif fecha == None or viv.comparar_fechas(fecha) and viv.comparar_estados_en_igual(menor_porciento):
                fecha = viv.fecha_inicio
                menor_porciento = viv.estado_de_terminacion
                datos = viv
        return datos

    # inc e porciento de viviendas que se están construyendo en un reparto dado con un tipo de cubierta dada con
    # garaje.      OK
    def indice_de_vivienda_por_reparto(self, reparto_dado):
        for indice in range(len(self.lista_vivienda)):
            if self.lista_vivienda[indice].es_reparto(reparto_dado):
                return indice

    def porciento_de_viviendas(self, techo_dado, reparto_dado):
        total_viviend = 0
        viviend = 0

        for vivienda in self.lista_vivienda_independiente():
            if vivienda.es_reparto(reparto_dado):
                total_viviend += 1
                if vivienda.es_techo(techo_dado) and vivienda.cochera:
                    viviend += 1
        return int((viviend * 100) / total_viviend)

    # inc f Listado de datos de apartamentos de un edificio dado su dirección ordenado por el porciento de
    # terminación menor a mayor.   OK
    def listado_de_datos(self, direccion_dada):
        listado_de_datos = []

        for vivienda in self.lista_vivienda_edificio():
            if vivienda.comparar_direccion_edificio(direccion_dada):
                listado_de_datos.append(vivienda)
        listado_de_datos.sort(key=attrgetter('estado_de_terminacion'))
        return listado_de_datos
