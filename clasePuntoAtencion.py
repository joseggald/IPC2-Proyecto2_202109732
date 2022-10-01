import string


class PuntoAtencion():
    idPuntoAtencion:string
    def __init__(self, idPuntoAtencion, nombre, direccion, escritorios, clientes):
        self.idPuntoAtencion=idPuntoAtencion
        self.nombre=nombre
        self.direccion=direccion
        self.escritorios=escritorios
        self.clientes=clientes  

       