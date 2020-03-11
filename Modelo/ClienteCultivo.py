class ClienteCultivo:
    idClienteCultivo = None
    extension = None
    ubicacion = None
    idCliente = None
    idCultivo = None
    idCiudad = None
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    def __init__(self,idClienteCultivo,extension,ubicacion,idCliente,idCultivo,idCiudad):
=======
    estatus = None
    def __init__(self,idClienteCultivo,extension,ubicacion,idCliente,idCultivo,idCiudad,estatus):
>>>>>>> Stashed changes
=======
    estatus = None
    def __init__(self,idClienteCultivo,extension,ubicacion,idCliente,idCultivo,idCiudad,estatus):
>>>>>>> Stashed changes
        self.idClienteCultivo = idClienteCultivo
        self.extension = extension
        self.ubicacion = ubicacion
        self.idCliente = idCliente
        self.idCultivo = idCultivo
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        self.idCiudad = idCiudad
=======
        self.idCiudad = idCiudad
        self.estatus = estatus
>>>>>>> Stashed changes
=======
        self.idCiudad = idCiudad
        self.estatus = estatus
>>>>>>> Stashed changes
