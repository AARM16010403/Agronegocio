class ClienteCultivo:
    idClienteCultivo = None
    extension = None
    ubicacion = None
    idCliente = None
    idCultivo = None
    idCiudad = None
    def __init__(self,idClienteCultivo,extension,ubicacion,idCliente,idCultivo,idCiudad):
        self.idClienteCultivo = idClienteCultivo
        self.extension = extension
        self.ubicacion = ubicacion
        self.idCliente = idCliente
        self.idCultivo = idCultivo
        self.idCiudad = idCiudad