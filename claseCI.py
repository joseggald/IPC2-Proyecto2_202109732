import string

class ConfigInicial():
    idConfig:string
    def __init__(self, idConfig,idEmpresa,idPunto,escritoriosActivos,clientes):
        self.idConfig=idConfig
        self.idEmpresa=idEmpresa
        self.idPunto=idPunto
        self.escritoriosActivos=escritoriosActivos
        self.clientes=clientes