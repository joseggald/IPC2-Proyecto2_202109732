from ListaSimple import Lista_simple


class PuntoAtencion():
    escritorios=Lista_simple
    def __init__(self, idPuntoAtencion, nombre, direccion, escritorios):
        self.idPuntoAtencion=idPuntoAtencion
        self.nombre=nombre
        self.direccion=direccion
        self.escritorios=escritorios

       