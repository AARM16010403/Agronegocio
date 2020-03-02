import pyodbc
from Datoss.Conexion import Conexion
from Modelo.Cliente import Cliente
from Modelo.UnidadTrans import UnidadTrans


class ClientesDAO:
    db = None
    def __init__(self):
        conx = Conexion()
        self.db = conx.getDB()
    def obtenerClientes(self):
        sql = "select idCliente,nombre,razonSocial,limiteCredito,direccion," \
              "codigoPostal,rfc,telefono,email,tipo,idCiudad from Ventas.Clientes where estatus = 'A'"
        lista = []
        try:
            cursor=self.db.cursor()
            cursor.execute(sql);
            data = cursor.fetchall()
            for dato in data:
<<<<<<< Updated upstream
<<<<<<< HEAD
=======
>>>>>>> Stashed changes
                sql = "select nombre from RH.Ciudades where idCiudad=(?)"
                Values = [dato[10]]
                cursor.execute(sql,Values)
                row = cursor.fetchone()
                dato[10] = row[0]
                fila = {"id":dato[0],"nombre":dato[1],"razon":dato[2],"limite":dato[3],"direccion":dato[4],
                        "codigo":dato[5],"rfc":dato[6],"telefono":dato[7],"email":dato[8],"tipo":dato[9],"ciudad":dato[10]}
<<<<<<< Updated upstream
=======
                fila = {"id":dato[0],"nombre":dato[1],"razon":dato[2],"limite":dato[3],"direccion":dato[4],
                        "codigo":dato[5],"rfc":dato[6],"tel":dato[7],"email":dato[8],"tipo":dato[9],"ciudad":dato[10]}
>>>>>>> d070e01b60ecf41de2efd276acde0aac9b6a9dc0
=======
>>>>>>> Stashed changes
                lista.append(fila)
            cursor.close()
            self.db.close()
        except pyodbc.Error as error:
            print(error)
        return lista
    def insertarCliente(self,cliente):
        sql = 'insert Ventas.Clientes (idCliente,nombre,razonSocial,limiteCredito,direccion,codigoPostal,' \
              'rfc,telefono,email,tipo,idCiudad,estatus) values (?,?,?,?,?,?,?,?,?,?,?,?)'
        try:
            Values = [cliente.idCliente,cliente.nombre,cliente.razonSocial,cliente.limiteCredito,cliente.direccion,
<<<<<<< Updated upstream
<<<<<<< HEAD
                      cliente.codigoPostal,cliente.rfc,cliente.telefono,cliente.email,cliente.tipo,cliente.idCiudad,cliente.estatus]
=======
                      cliente.codigoPostal,cliente.rfc,cliente.telefono,cliente.email,cliente.tipo,cliente.idCiudad]
>>>>>>> d070e01b60ecf41de2efd276acde0aac9b6a9dc0
=======
                      cliente.codigoPostal,cliente.rfc,cliente.telefono,cliente.email,cliente.tipo,cliente.idCiudad,cliente.estatus]
>>>>>>> Stashed changes
            cursor=self.db.cursor()
            cursor.execute(sql,Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as error:
            print(error)
    def ultimoID(self):
        sql="select max(idCliente)+1 id from Ventas.Clientes"
        id=1
        try:
            cursor=self.db.cursor()
            cursor.execute(sql)
            rs=cursor.fetchone()
            id=rs[0]
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
        return id
    def consultaIndividual(self,id):
        sql = 'select idCliente,nombre,razonSocial,limiteCredito,direccion,' \
              'codigoPostal,rfc,telefono,email,tipo,idCiudad from Ventas.Clientes where idCliente=(?)'
        c=None
        try:
            cursor = self.db.cursor()
            Values = [id]
            cursor.execute(sql,Values)
            rs = cursor.fetchone()
            c = Cliente(rs[0], rs[1], rs[2], rs[3],rs[4],rs[5],rs[6],rs[7],rs[8],rs[9],rs[10],'A')
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
        return c
    def actualizar(self,cliente):
        sql = "update Ventas.Clientes set nombre=(?),razonSocial=(?),limiteCredito=(?),direccion=(?),codigoPostal=(?), " \
              "rfc=(?),telefono=(?),email=(?),tipo=(?),idCiudad=(?) where idCliente=(?)"
        try:
            cursor = self.db.cursor()
            Values = [cliente.nombre,cliente.razonSocial,cliente.limiteCredito,cliente.direccion,
                      cliente.codigoPostal,cliente.rfc,cliente.telefono,cliente.email,cliente.tipo,cliente.idCiudad,cliente.idCliente]
            cursor.execute(sql,Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
    def eliminar(self,id):
        sql="update Ventas.Clientes set estatus='I' where idCliente=(?)"
        try:
            cursor = self.db.cursor()
            Values = [id]
            cursor.execute(sql, Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)