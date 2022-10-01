import string


class Clientes():
    dpi:string
    def __init__(self, dpi, nombre, transacciones, cantidad):
        self.dpi=dpi
        self.nombre=nombre
        self.transacciones=transacciones
        self.cantidad=cantidad