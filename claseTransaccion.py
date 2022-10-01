import string


class Transaccion():
    idTrans:string
    def __init__(self, idTrans, nombre, tiempo):
        self.nombre=nombre
        self.idTrans=idTrans
        self.tiempo=tiempo