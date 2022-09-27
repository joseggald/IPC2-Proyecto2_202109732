from ListaSimple import Lista_simple


class Empresa():
    puntosAtencion=Lista_simple
    transacciones=Lista_simple
    def __init__(self, idEmpresa, nombre, abreviatura, puntosAtencion, transacciones):
        self.idEmpresa=idEmpresa
        self.nombre=nombre
        self.abreviatura=abreviatura
        self.puntosAtencion=puntosAtencion
        self.transacciones=transacciones
