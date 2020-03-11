class OfertaAsociacion:
    idAsociacion = None
    idOferta = None
    estatus = None
    def __init__(self,idAsociacion,idOferta,estatus):
        self.idAsociacion=idAsociacion
        self.idOferta=idOferta
        self.estatus=estatus