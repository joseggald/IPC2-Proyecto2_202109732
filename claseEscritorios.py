import string


class Escritorio():
    idEsc:string
    def __init__(self, idEsc, identificacion, encargado, estado):
        self.idEsc=idEsc
        self.identificacion=identificacion
        self.encargado=encargado
        self.estado=estado    