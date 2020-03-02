class Cultivo:
    idCultivo=None
    nombre=None
    costoAsesoria=None
    estatus=None
    def __init__(self,idCultivo,nombre,costoAsesoria,estatus):
        self.idCultivo=idCultivo
        self.nombre=nombre
        self.costoAsesoria=costoAsesoria
        self.estatus=estatus