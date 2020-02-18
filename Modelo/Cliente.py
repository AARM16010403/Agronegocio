class Cliente:
    idCliente=None
    nombre=None
    razonSocial=None
    limiteCredito=None
    direccion=None
    codigoPostal=None
    rfc=None
    telefono=None
    email=None
    tipo=None
    idCiudad=None
    estatus=None
    def __init__(self,idCliente,nombre,razonSocial,limiteCredito,direccion,codigoPostal,rfc,telefono,email,tipo,idCiudad,estatus):
        self.idCliente=idCliente
        self.nombre=nombre
        self.razonSocial=razonSocial
        self.limiteCredito=limiteCredito
        self.direccion=direccion
        self.codigoPostal=codigoPostal
        self.rfc=rfc
        self.telefono=telefono
        self.email=email
        self.tipo=tipo
        self.idCiudad=idCiudad
        self.estatus=estatus
