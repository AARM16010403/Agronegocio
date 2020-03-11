class Oferta:
    idOferta = None
    nombre = None
    descripcion = None
    porDescuento = None
    fechaInicio = None
    fechaFin = None
    canMinProducto = None
    estatus = None
    idProducto = None
    def __init__(self,idOferta,nombre,descripcion,porDescuento,fechaInicio,fechaFin,canMinProducto,estatus,idProducto):
        self.idOferta=idOferta
        self.nombre=nombre
        self.descripcion=descripcion
        self.porDescuento=porDescuento
        self.fechaInicio=fechaInicio
        self.fechaFin=fechaFin
        self.canMinProducto=canMinProducto
        self.estatus=estatus
        self.idProducto=idProducto
