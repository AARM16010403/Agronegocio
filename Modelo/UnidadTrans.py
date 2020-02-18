class UnidadTrans:
    idUnidadTransporte=None
    placas=None
    marca=None
    modelo=None
    anio=None
    capacidad=None
    estatus=None
    def __init__(self,idUnidadTransporte,placas,marca,modelo,anio,capacidad,estatus):
        self.idUnidadTransporte=idUnidadTransporte
        self.placas=placas
        self.marca=marca
        self.modelo=modelo
        self.anio=anio
        self.capacidad=capacidad
        self.estatus=estatus
