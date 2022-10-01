
import string

class Empresa():
    idEmpresa:string
    def __init__(self, idEmpresa, nombre, abreviatura, puntosAtencion, transacciones):
        self.idEmpresa=idEmpresa
        self.nombre=nombre
        self.abreviatura=abreviatura
        self.puntosAtencion=puntosAtencion
        self.transacciones=transacciones
        
