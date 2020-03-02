class Miembro:
    idCliente=None
    idAsociacion=None
    estatus=None
    fechaIncorporacion=None
    def __init__(self,idCliente,idAsociacion,estatus,fechaIncorporacion):
        self.idCliente=idCliente
        self.idAsociacion=idAsociacion
        self.estatus=estatus
        self.fechaIncorporacion=fechaIncorporacion